@echo off
title Free Games Claimer - Sofort-Test
cd /d "%~dp0"
set PYTHONUTF8=1

echo ========================================================
echo   FREE GAMES CLAIMER - TESTLAUF
echo ========================================================
echo   Prueft alle Stores nach Gratis-Spielen...
echo   Nach Abschluss erhaeltst du die Discord-Nachricht!
echo ========================================================
echo.

.\venv\Scripts\python.exe main.py --once
echo.
echo ========================================================
echo   Durchlauf beendet! Schau in deinen Discord-Kanal.
echo   Ein vollstaendiges Log findest du in: data\claimer.log
echo ========================================================
pause

