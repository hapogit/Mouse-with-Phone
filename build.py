"""
🔨 Liquid Mouse Builder
Questo script crea l'eseguibile standalone (EXE) per Windows.
"""
import os
import subprocess
import sys
import shutil

def check_files():
    """Verifica la presenza dei file essenziali"""
    required = ["server.pyw", "index.html"]
    missing = [f for f in required if not os.path.exists(f)]
    
    if missing:
        print(f"❌ Errore: Mancano i seguenti file: {', '.join(missing)}")
        return False
    return True

def build():
    print("="*50)
    print("   🖱️  LIQUID MOUSE BUILDER")
    print("="*50)

    # 1. Installa PyInstaller se necessario
    print("\n📦 Verifica PyInstaller...")
    try:
        import PyInstaller
        print("   ✅ PyInstaller trovato.")
    except ImportError:
        print("   ⬇️  Installazione PyInstaller in corso...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

    # 2. Configurazione Build
    if not check_files():
        return

    # Opzioni PyInstaller
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--noconsole",              # Niente finestra nera cmd
        "--onefile",                # Unico file .exe
        "--name", "LiquidMouse",    # Nome output
        "--clean",                  # Pulisci cache
        "--log-level", "WARN",
        
        # Includi index.html nella root dell'exe
        "--add-data", "index.html;.", 
    ]

    # Aggiungi icona se esiste
    if os.path.exists("icon.ico"):
        print("   🎨 Icona trovata: icon.ico")
        cmd.extend(["--icon", "icon.ico", "--add-data", "icon.ico;."])
    else:
        print("   ⚠️  Icona non trovata (verrà usata quella di default)")

    cmd.append("server.pyw")

    # Pulizia preventiva: Rimuove il vecchio EXE se esiste
    exe_out = os.path.join("dist", "LiquidMouse.exe")
    if os.path.exists(exe_out):
        try:
            os.remove(exe_out)
            print("   🗑️  Vecchia versione rimossa.")
        except OSError:
            print(f"\n❌ ERRORE: Impossibile sovrascrivere il file.")
            print("   ⚠️  Sembra che Liquid Mouse sia ancora APERTO. Chiudilo e riprova.")
            return

    # 3. Esecuzione
    print("\n🚀 Avvio compilazione (potrebbe richiedere qualche minuto)...")
    try:
        subprocess.check_call(cmd)
        print("\n✅ BUILD COMPLETATA CON SUCCESSO!")
        
        exe_path = os.path.abspath(os.path.join("dist", "LiquidMouse.exe"))
        print(f"\n📂 Il tuo file è pronto qui:\n   {exe_path}")
        
    except subprocess.CalledProcessError:
        print("\n❌ Errore durante la compilazione.")

if __name__ == "__main__":
    build()
    input("\nPremi Invio per uscire...")
