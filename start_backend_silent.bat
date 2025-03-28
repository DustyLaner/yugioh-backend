@echo off
echo Starte Yu-Gi-Oh! Backend für WLAN-Zugriff...
cd /d C:\Users\laein\yugioh_backend
start "" /min uvicorn main:app --host 0.0.0.0 --port 8000 --reload

timeout /t 2 >nul

echo Starte Yu-Gi-Oh! Frontend...
cd /d C:\Users\laein\yugioh_backend\yugioh-frontend
start "" /min npm start

timeout /t 3 >nul
echo Starte Browser auf dem PC...