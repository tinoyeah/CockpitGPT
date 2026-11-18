import datetime as dt
import json
import os
import re
import urllib.parse
import urllib.request

GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
MODEL = "gemini-2.5-flash"

QUERIES = [
    "BCE tassi inflazione eurozona OR geopolitica Iran Ucraina dazi USA",
    "TTF gas Brent PUN pomodoro zucchero caffè cacao grano",
    "FMCG food grocery Nestlé Danone Kraft Heinz Mutti",
    "corporate governance Consob OPA Prada Kering LVMH Moncler",
    "UK Germany France Poland Nordics USA Australia economy inflation grocery",
    "canoa slalom tennis Sinner WRC Formula 1 MotoGP",
]


def get_json(url):
    request = urllib.request.Request(url, headers={"User-Agent": "CFO-Cockpit/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def get_market_snapshot():
    try:
        return get_json("https://energyindex.it/api/v1/today")
    except Exception as exc:
        return {"error": str(exc)}


def clean_json(text):
    text = text.strip()
    text = re.sub(r"^```json\s*", "", text, flags=re.I)
    text = re.sub(r"\s*```$", "", text)
    return json.loads(text)


def generate():
    if not GEMINI_KEY:
        raise RuntimeError("GEMINI_API_KEY non configurata nei GitHub Secrets")

    try:
        with open("news.json", encoding="utf-8") as file:
            news = json.load(file).get("items", [])
    except Exception as exc:
        raise RuntimeError(f"news.json non disponibile: {exc}") from exc

    # Riduce duplicati mantenendo il primo titolo incontrato.
    unique = {}
    for item in news:
        key = re.sub(r"[^a-z0-9]", "", item["title"].lower())[:100]
        unique[key] = item
    news = list(unique.values())[:30]
    market = get_market_snapshot()

    prompt = """Sei il responsabile Group Business Controlling di un gruppo FMCG alimentare.
Prepara un briefing manageriale in italiano usando le notizie e i dati di mercato sotto.

Regole:
- non inventare fatti, numeri o implicazioni;
- separa chiaramente fatti osservati e interpretazioni;
- dai priorità a impatto su costi, margini, prezzi, domanda, supply chain, cambi e rischio;
- considera anche le notizie sulle filiali e lo sport, ma tratta lo sport in una breve sezione finale;
- sii concreto, leggibile in meno di due minuti e adatto a un CFO;
- restituisci esclusivamente JSON valido con questa struttura:
{"summary":"testo con paragrafi brevi","key_points":["...","..."],"risks":["..."],"opportunities":["..."],"sport":"..."}

DATI DI MERCATO:
""" + json.dumps(market, ensure_ascii=False) + "\n\nNOTIZIE:\n" + json.dumps(news, ensure_ascii=False)

    endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={urllib.parse.quote(GEMINI_KEY)}"
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.2, "responseMimeType": "application/json"},
    }
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": "CFO-Cockpit/1.0"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=90) as response:
        result = json.loads(response.read().decode("utf-8"))

    text = result["candidates"][0]["content"]["parts"][0]["text"]
    output = clean_json(text)
    output["date"] = dt.datetime.now(dt.timezone.utc).date().isoformat()
    output["cfo"] = []
    with open("summary.json", "w", encoding="utf-8") as file:
        json.dump(output, file, ensure_ascii=False, indent=2)
        file.write("\n")


if __name__ == "__main__":
    generate()
