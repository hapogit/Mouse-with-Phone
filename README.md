# 🖱️ Liquid Mouse v1.3.2

Liquid Mouse trasforma il tuo smartphone in un touchpad wireless fluido e professionale per il tuo computer, operante interamente sulla rete Wi-Fi locale.

## ✨ Funzionalità Principali

* **Fluid Touch:** Movimento del cursore a bassa latenza.
* **Smart Scrolling:** Scorrimento inerziale ad alta sensibilità.
* **Funzioni Avanzate:** Drag & Drop, Seleziona Tutto (Ctrl+A), Tastiera Remota.
* **Server GUI:** Interfaccia moderna con supporto System Tray e Icone Personalizzate.
* **Privacy First:** Nessun cloud, funziona solo sulla rete locale.

## ⚠️ Limitazioni Importanti

* **Schermata di Login/Blocco:** A causa delle restrizioni di sicurezza di Windows (Secure Desktop), l'applicazione **non può interagire** con la schermata di login o quando il PC è bloccato. È necessario utilizzare un mouse/tastiera fisica per inserire la password. Una volta effettuato l'accesso, Liquid Mouse inizierà a funzionare immediatamente.

## 🚀 Guida Rapida

1.  **Installazione Dipendenze:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Avvio Server:**
    Esegui il file `server.pyw`.
    Apparirà il pannello di controllo con l'indirizzo IP da utilizzare.

3.  **Connessione:**
    Apri il browser del tuo smartphone e digita l'indirizzo IP mostrato (es: `192.168.1.X:8000`).

## 📋 Changelog Recente (v1.3.2)

- **Custom Icons:** Supporto per icone personalizzate (.ico) nella finestra e nella tray.
- **System Tray:** Gestione migliorata del menu contestuale e minimizzazione.
- **Stabilità:** Controllo automatico dipendenze (Pillow, pystray) con avvisi grafici.
- **Core:** Ottimizzazione gestione percorsi e caricamento risorse.