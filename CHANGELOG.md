# Changelog

Tutti i cambiamenti importanti a questo progetto saranno documentati in questo file.

## [1.3.2] - 2026-01-15 (Stability & Typing)
### ✨ Aggiunto
- **Typing:** Supporto automatico per "smart quotes" (virgolette curve) da mobile.
- **Debounce:** Filtro anti-rimbalzo per il tasto Backspace (evita cancellazioni doppie involontarie).
- **Sicurezza:** Chiusura forzata pulita dell'applicazione (`os._exit`).

### 🔧 Modificato
- **Docs:** Aggiornata documentazione con avvisi su Secure Desktop (Login Windows).
- **Core:** Ottimizzazione gestione percorsi e caricamento risorse.

## [1.2.0] - 2026-01-14 (Tray Edition)
### ✨ Aggiunto
- **GUI (Interfaccia Grafica):** Sostituito il terminale nero con una finestra moderna in stile Liquid Mouse.
- **System Tray:** Il server ora si riduce a icona nella barra delle applicazioni invece di chiudersi.
- **Drag & Drop:** Nuovo pulsante "Lucchetto" per trascinare finestre e oggetti.
- **Select All:** Nuovo pulsante "SEL ALL" per selezionare tutto (Ctrl+A).

### 🔧 Modificato
- **Scroll:** Aumentata notevolmente la sensibilità dello scroll verticale per maggiore fluidità.
- **Design:** Migliorata leggibilità nella pagina di configurazione (testo bianco su sfondo scuro).
- **Stabilità:** Aggiunto rilascio automatico del mouse in caso di disconnessione durante il trascinamento.

## [1.0.0] - 2026-01-12
### ✨ Aggiunto
- Versione stabile iniziale del progetto.
- Server WebSocket base.
- Interfaccia web responsive.