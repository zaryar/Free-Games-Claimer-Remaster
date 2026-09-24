@echo off
title Autostart Einrichten (Windows-Aufgabenplanung)
echo ========================================================
echo   Richte Autostart bei PC-Start ein...
echo ========================================================

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$action = New-ScheduledTaskAction -Execute '%~dp0venv\Scripts\python.exe' -Argument 'main.py --once' -WorkingDirectory '%~dp0';" ^
  "$trigger = New-ScheduledTaskTrigger -AtLogOn -User '$env:USERNAME';" ^
  "$trigger.Delay = 'PT1M';" ^
  "$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable;" ^
  "Register-ScheduledTask -TaskName 'FreeGamesClaimer_OnBoot' -Action $action -Trigger $trigger -Settings $settings -Force"

echo.
echo ========================================================
echo   [OK] Autostart ist aktiv!
echo   Der Claimer startet ab sofort bei jedem PC-Start lautlos
echo   im Hintergrund (1 Minute Verzoegerung fuers Hochfahren),
echo   sendet die Discord-Nachricht und beendet sich danach sofort.
echo ========================================================
pause
