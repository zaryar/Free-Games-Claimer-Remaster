# 🎮 Free Games Claimer (Windows PC)

Der Free Games Claimer läuft direkt auf deinem Windows-PC, beansprucht vollautomatisch Gratis-Spiele und Assets von Steam, Epic Games, Fab (Epic 3D Assets), GOG, Prime Gaming und Ubisoft, überwacht Alienware Arena Giveaways und sendet das Ergebnis an deinen Discord-Kanal.

---

## 🏬 Unterstützte Stores & Plattformen

| Store | Status | Typ | Login / Voraussetzung |
| :--- | :--- | :--- | :--- |
| **Steam** | ✅ Aktiv | Auto-Claim | Steam-Login (SteamDB + GamerPower) |
| **Epic Games** | ✅ Aktiv | Auto-Claim | Epic-Login (PC- & Handy-Games `EG_MOBILE`) |
| **Fab (Epic Assets)** | ✅ Aktiv | Auto-Claim | Nutzt direkt dein bestehendes Epic-Profil! |
| **GOG** | ✅ Aktiv | Auto-Claim | GOG-Login + löst Amazon Prime GOG-Keys ein |
| **Prime Gaming** | ✅ Aktiv | Auto-Claim | Amazon-Login |
| **Ubisoft** | ✅ Aktiv | Auto-Claim | Ubisoft-Login |
| **Alienware Arena** | ✅ Aktiv | **Notify-Only** | Schickt Discord-Alerts für Steam-Keys (benötigt ARP-Punkte auf der Website) |
| *Itch.io* | ⚙️ Optional | Auto-Claim | Vorab einmalig einloggen via `EINMALIG_EINLOGGEN.bat` [6] |
| *Fanatical* | ⚙️ Optional | Auto-Claim | Fanatical-Account mit verknüpftem Steam-Account; Login via [7] |
| *IndieGala* | ⚙️ Optional | Auto-Claim | IndieGala-Account; Login via [8] |
| *Unity Asset Store* | ⚙️ Optional | Auto-Claim | Unity-Account mit Rechnungsadresse; Login via [9] |
| *AliExpress* | ⚙️ Optional | Münz-Check-in | Täglicher Münz-Check-in via [10] |
| *Microsoft Store* | ⚙️ Optional | Auto-Claim | Microsoft-Account; Login via [11] oder `MS_EMAIL`/`MS_PASSWORD` in `.env` |

---

## ⚡ So funktioniert die Automatik bei PC-Start
* **Windows-Aufgabenplanung:** Ist bereits als Aufgabe `FreeGamesClaimer_OnBoot` eingerichtet!
* **Ablauf:**
  1. Du fährst deinen PC hoch und meldest dich an.
  2. Nach **1 Minute Wartezeit** (damit dein PC in Ruhe hochfahren kann und WLAN/LAN stabil verbunden sind) startet der Bot **vollständig unsichtbar im Hintergrund**.
  3. Kein Browserfenster poppt auf, kein schwarzes Konsolenfenster stört beim Zocken.
  4. Der Bot prüft alle Stores und sendet die Discord-Nachricht:
     * Wenn Spiele/Assets geclaimt oder gemeldet wurden: Liste der gesicherten Spiele.
     * Wenn keine neuen Spiele da sind:  
       `⚠️ Free Games Claimer (PC-Start): Warnung, keine Games da! Aktuell sind alle deine Stores auf dem neuesten Stand.`
  5. **Der Bot beendet sich sofort nach dem Durchlauf.** (Verbraucht 0 MB RAM und 0% CPU beim Zocken).

---

## 🛠️ Wichtige Steuerungsdateien

| Datei | Zweck |
| :--- | :--- |
| **`EINMALIG_EINLOGGEN.bat`** | Öffnet das Login-Menü. Öffnet echtes Chrome auf deinem Desktop für Steam, Epic, GOG, Itch.io, Fanatical etc. (0 Lag). |
| **`START_SOFORT_TEST.bat`** | Startet sofort einen Durchlauf mit Konsolenfenster zum Testen. |
| **`AUTOSTART_EINRICHTEN.bat`** | Aktiviert oder erneuert die Windows-Startaufgabe. |
| **`AUTOSTART_ENTFERNEN.bat`** | Löscht die Windows-Startaufgabe komplett. |

