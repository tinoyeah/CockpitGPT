import datetime as dt
import json
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

QUERIES = {
    "vertici": "nomina nuovo CEO OR CFO OR amministratore delegato alimentare OR food OR largo consumo OR lusso OR moda",
    "macro": "BCE tassi inflazione eurozona OR geopolitica Iran Ucraina dazi USA",
    "materie": "prezzo cacao OR caffè OR zucchero OR grano OR pomodoro mercato commodity",
    "fmcg": "FMCG food grocery Nestle Danone Kraft Heinz Mutti",
    "gov": "corporate governance Consob OPA Prada Kering LVMH Moncler",
    "filiali": "UK Germany France Poland Nordics USA Australia economy inflation grocery",
    "sport_canoa_slalom": "canoa slalom",
    "sport_tennis": "ATP Slam Masters 1000 Sinner Cobolli",
    "sport_wrc": "WRC rally mondiale",
    "sport_formula_1": "Formula 1 F1 mondiale",
    "sport_motogp": "MotoGP mondiale",
}


def get_feed(category, query):
    rss = "https://news.google.com/rss/search?q=" + urllib.parse.quote(query + " when:3d") + "&hl=it&gl=IT&ceid=IT:it"
    request = urllib.request.Request(rss, headers={"User-Agent": "Mozilla/5.0 CFO-Cockpit/2.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        root = ET.fromstring(response.read())
    result = []
    for item in root.findall("./channel/item")[:12]:
        title = item.findtext("title", "").strip()
        link = item.findtext("link", "").strip()
        pub_date = item.findtext("pubDate", "").strip()
        if title and link:
            result.append({"title": title, "link": link, "pubDate": pub_date, "category": category})
    return result


def main():
    items = []
    for category, query in QUERIES.items():
        try:
            items.extend(get_feed(category, query))
        except Exception as exc:
            print(f"Feed non disponibile ({category}): {exc}")

    unique = {}
    for item in items:
        key = re.sub(r"[^a-z0-9]", "", item["title"].lower())[:120]
        unique.setdefault(key, item)

    if not unique:
        try:
            with open("news.json", encoding="utf-8") as file:
                previous = json.load(file)
            print("Nessun feed disponibile: mantengo le news precedenti")
            return
        except Exception:
            pass

    output = {"updated_at": dt.datetime.now(dt.timezone.utc).isoformat(), "items": list(unique.values())}
    with open("news.json", "w", encoding="utf-8") as file:
        json.dump(output, file, ensure_ascii=False, indent=2)
        file.write("\n")
    print(f"Salvate {len(output['items'])} news")


if __name__ == "__main__":
    main()
