@echo off
title Free Games Claimer - Store Login Assistent (PC)
cd /d "%~dp0"
set PYTHONUTF8=1

echo ========================================================
echo   FREE GAMES CLAIMER - STORE LOGIN ASSISTENT (PC)
echo ========================================================
echo   Hier kannst du dich 1-mal ganz normal in Chrome einloggen.
echo   Kein Lag, direkt auf deinem PC mit voller Geschwindigkeit!
echo ========================================================
echo.

.\venv\Scripts\python.exe login_helper.py
pause
