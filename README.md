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

Le notizie vengono recuperate tramite Google News RSS e il proxy rss2json. Le fonti sono curate nella configurazione tramite query con priorità editoriale; Google News resta un fallback e un aggregatore.

I cambi vengono recuperati da Frankfurter, che utilizza i tassi BCE. Budget, EBITDA, note, letture e articoli salvati restano nel local storage del dispositivo.

`summary.json` è opzionale. Se presente nella stessa cartella, deve contenere la sintesi manageriale complessiva di prezzi, news, filiali e sport:

```json
{
  "date": "2026-11-15",
  "summary": "Testo del briefing del giorno.",
  "cfo": ["Prima domanda", "Seconda domanda"]
}
```

## Nota tecnica

Per il funzionamento completo, usare GitHub Pages o un altro server HTTPS. Il service worker non viene registrato correttamente aprendo il file direttamente dal computer con `file://`.
