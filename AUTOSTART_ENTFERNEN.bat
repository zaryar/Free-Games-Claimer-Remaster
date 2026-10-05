@echo off
title Autostart Entfernen (Windows-Aufgabenplanung)
echo ========================================================
echo   Entferne Autostart bei PC-Start...
echo ========================================================

powershell -NoProfile -ExecutionPolicy Bypass -Command "Unregister-ScheduledTask -TaskName 'FreeGamesClaimer_OnBoot' -Confirm:$false -ErrorAction SilentlyContinue"

echo [OK] Autostart wurde vollstaendig entfernt!
pause
