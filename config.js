/* Configurazione editoriale: modificare qui fonti, temi e filiali. */
const CONFIG = {
  cacheMinutes: 30,
  maxArticlesPerTheme: 5,
  newsProxy: "https://api.rss2json.com/v1/api.json?rss_url=",
  currencies: ["GBP", "USD", "AUD", "PLN", "SEK", "NOK"],
  currencyNames: { GBP: "Regno Unito", USD: "USA", AUD: "Australia", PLN: "Polonia", SEK: "Nordici", NOK: "Nordici" },
  sources: {
    bce: { name: "BCE", priority: 5, query: "site:ecb.europa.eu" },
    eurostat: { name: "Eurostat", priority: 5, query: "site:ec.europa.eu/eurostat" },
    reuters: { name: "Reuters", priority: 4, query: "site:reuters.com" },
    ft: { name: "Financial Times", priority: 4, query: "site:ft.com" },
    official: { name: "Fonti ufficiali", priority: 5, query: "" },
    google: { name: "Google News", priority: 1, query: "" }
  },
  themes: [
    { id: "vertici", title: "Movimenti ai vertici", when: "30d", feeds: [{ source: "google", query: "nomina nuovo CEO OR CFO OR amministratore delegato alimentare OR food OR largo consumo OR lusso OR moda" }] },
    { id: "macro", title: "Macro e geopolitica", when: "2d", feeds: [
      { source: "bce", query: "BCE tassi inflazione eurozona" },
      { source: "eurostat", query: "Eurostat inflation GDP euro area" },
      { source: "reuters", query: "geopolitica Iran Hormuz Ucraina dazi USA" }
    ] },
    { id: "materie", title: "Materie prime", when: "3d", feeds: [
      { source: "reuters", query: "prezzo cacao OR caffè OR zucchero OR grano OR pomodoro mercato" },
      { source: "google", query: "commodity prices tomato wheat sugar coffee cocoa" }
    ] },
    { id: "fmcg", title: "Corporate e FMCG", when: "3d", feeds: [
      { source: "reuters", query: "FMCG food grocery Nestle Danone Kraft Heinz" },
      { source: "google", query: "largo consumo food NielsenIQ OR Circana OR Ipsos OR Mutti" }
    ] },
    { id: "gov", title: "Governance e lusso", when: "3d", feeds: [
      { source: "official", query: "corporate governance assemblea CDA Consob OPA Piazza Affari" },
      { source: "google", query: "lusso moda Prada OR Kering OR LVMH OR Moncler" }
    ] },
    { id: "sport", title: "Sport", when: "14d", feeds: [
      { source: "google", query: "canoa slalom OR ATP Slam OR Masters 1000 OR Sinner OR Cobolli OR WRC rally mondiale" }
    ] }
  ],
  branches: [
    { name: "Regno Unito", currencies: ["GBP"], query: "UK economy OR inflation OR Bank of England OR grocery Tesco OR Sainsbury's" },
    { name: "Germania", currencies: [], query: "Germany economy OR inflation OR Bundesbank OR Ifo OR budget" },
    { name: "Francia e Benelux", currencies: [], query: "France OR Netherlands OR Belgium economy OR inflation OR budget OR strike" },
    { name: "Polonia", currencies: ["PLN"], query: "Poland economy OR inflation OR zloty OR NBP" },
    { name: "Paesi nordici", currencies: ["SEK", "NOK"], query: "Sweden OR Norway OR Denmark OR Finland economy OR Riksbank OR Norges Bank OR inflation" },
    { name: "USA", currencies: ["USD"], query: "US economy OR Fed OR inflation OR tariffs OR consumer spending grocery" },
    { name: "Australia", currencies: ["AUD"], query: "Australia economy OR RBA OR inflation OR Woolworths OR Coles" }
  ],
  sports: [
    { title: "Canoa slalom", query: "canoa slalom" },
    { title: "Tennis", query: "ATP Slam OR Masters 1000 OR Sinner OR Cobolli" },
    { title: "WRC", query: "WRC rally mondiale" },
    { title: "Formula 1", query: "Formula 1 F1 mondiale" },
    { title: "MotoGP", query: "MotoGP mondiale" }
  ],
  questions: [
    "Quali costi stanno uscendo dal budget e perché?",
    "Dove vedi pressione sui prezzi o sulla marca del distributore?",
    "Qual è oggi il rischio principale sul forecast del trimestre?",
    "Cosa ti serve da me o dal gruppo questo mese?",
    "Quali segnali anticipano il primo trimestre del prossimo anno?",
    "Che cosa dicono i clienti della distribuzione su promozioni e listini?",
    "Quale decisione stai rimandando e cosa ti serve per prenderla?",
    "Cosa ha funzionato meglio del previsto negli ultimi due mesi?"
  ]
};
