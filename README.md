# Cockpit CFO

Mini-app statica per briefing quotidiano, esposizione cambi, notizie per tema e preparazione delle call con le filiali.

## Struttura

- Sintesi: briefing manageriale aggregato da `summary.json`.
- Prezzi: cambi e metriche già presenti nel cockpit.
- News: notizie economiche e corporate per tema.
- Filiali: preparazione delle call e notizie locali.
- Sport: canoa slalom, tennis, WRC, Formula 1 e MotoGP.
- Radar: articoli salvati per la discussione.

## Pubblicazione su GitHub Pages

1. Caricare tutti i file di questa cartella nella root del repository oppure in una cartella pubblicata.
2. In GitHub: **Settings → Pages → Deploy from a branch**.
3. Selezionare il branch principale e la cartella `/root`.
4. Aprire l’URL generato da GitHub Pages.

## Configurazione

Modificare `config.js` per cambiare temi, query, fonti, filiali e domande per le call.

Le notizie vengono raccolte da GitHub Actions e salvate in `news.json`. L’app legge il file locale, evitando dipendenze dal browser, CORS e dal proxy `rss2json`. Le query sono definite in `scripts/collect_news.py`.

I cambi vengono recuperati da Frankfurter, che utilizza i tassi BCE. Budget, EBITDA, note, letture e articoli salvati restano nel local storage del dispositivo.

`summary.json` deve trovarsi nella stessa cartella di `v4.html` e `index.html`. È il file che alimenta la sintesi manageriale complessiva di prezzi, news, filiali e sport:

```json
{
  "date": "2026-11-15",
  "summary": "Testo del briefing del giorno.",
  "cfo": ["Prima domanda", "Seconda domanda"]
}
```

## Frase del giorno

La tab Sintesi legge `quotes.json` e seleziona una sola frase al giorno usando la data del dispositivo. Il database contiene 500 schede con autore, libro, tema e tipo della frase. Le schede attuali sono esplicitamente marcate come frasi originali ispirate; non vengono presentate come citazioni testuali verificate.

`summary.json` resta disponibile come fallback, ma non è più necessario per mostrare la frase del giorno.

## Aggiornamento automatico di news e sintesi

Il file `.github/workflows/update-summary.yml` aggiorna automaticamente `news.json` e `summary.json` ogni giorno. Per attivarlo:

1. Crea una chiave in Google AI Studio.
2. In GitHub vai su **Settings → Secrets and variables → Actions**.
3. Crea un nuovo repository secret chiamato `GEMINI_API_KEY` e incolla la chiave.
4. Vai nella tab **Actions**, seleziona **Aggiorna sintesi manageriale** e premi **Run workflow**.

Dopo l’esecuzione, GitHub farà un commit automatico dei file aggiornati; GitHub Pages mostrerà le nuove news al successivo aggiornamento della pagina.

## Nota tecnica

Per il funzionamento completo, usare GitHub Pages o un altro server HTTPS. Il service worker non viene registrato correttamente aprendo il file direttamente dal computer con `file://`.
