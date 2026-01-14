@echo off
REM Script per aggiungere Liquid Mouse all'avvio automatico di Windows

set "TARGET=%~dp0start.bat"
set "WORK_DIR=%~dp0"
set "ICON=%~dp0icon.ico"
set "SHORTCUT=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\Liquid Mouse.lnk"
set "PWS=powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile"

echo [INFO] Configurazione avvio automatico in corso...
%PWS% -Command "$ws = New-Object -ComObject WScript.Shell; $s = $ws.CreateShortcut('%SHORTCUT%'); $s.TargetPath = '%TARGET%'; $s.WorkingDirectory = '%WORK_DIR%'; $s.IconLocation = '%ICON%'; $s.WindowStyle = 7; $s.Save()"

if exist "%SHORTCUT%" (
    echo [OK] Liquid Mouse e' stato aggiunto all'avvio di Windows!
) else (
    echo [ERRORE] Qualcosa e' andato storto. Prova il metodo manuale.
)
pause