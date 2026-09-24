#!/usr/bin/env python3
"""Interactive store login helper for Free Games Claimer Remaster on Windows PC.
Opens native Google Chrome with full GPU acceleration directly on your desktop (0 lag).
"""

import asyncio
import os
import sys
from pathlib import Path
import nodriver as uc

BASE_DIR = Path(__file__).resolve().parent
DATA_BROWSER_DIR = BASE_DIR / "data" / "browser"

STORES = {
    "1": {
        "name": "Epic Games",
        "key": "epic",
        "url": "https://store.epicgames.com/login",
        "profile": DATA_BROWSER_DIR / "epic",
    },
    "2": {
        "name": "Steam",
        "key": "steam",
        "url": "https://store.steampowered.com/login/",
        "profile": DATA_BROWSER_DIR / "steam",
    },
    "3": {
        "name": "GOG",
        "key": "gog",
        "url": "https://www.gog.com/account",
        "profile": DATA_BROWSER_DIR / "gog",
    },
    "4": {
        "name": "Amazon / Prime Gaming",
        "key": "prime",
        "url": "https://luna.amazon.com/claims/home",
        "profile": DATA_BROWSER_DIR / "prime",
    },
    "5": {
        "name": "Ubisoft",
        "key": "ubisoft",
        "url": "https://account.ubisoft.com/en-US/account-information",
        "profile": DATA_BROWSER_DIR / "ubisoft",
    },
    "6": {
        "name": "Itch.io",
        "key": "itchio",
        "url": "https://itch.io/login",
        "profile": DATA_BROWSER_DIR / "base",
    },
    "7": {
        "name": "Fanatical",
        "key": "fanatical",
        "url": "https://www.fanatical.com/",
        "profile": DATA_BROWSER_DIR / "base",
    },
    "8": {
        "name": "IndieGala",
        "key": "indiegala",
        "url": "https://www.indiegala.com/login",
        "profile": DATA_BROWSER_DIR / "base",
    },
    "9": {
        "name": "Unity Asset Store",
        "key": "unity",
        "url": "https://assetstore.unity.com/orders",
        "profile": DATA_BROWSER_DIR / "unity",
    },
    "10": {
        "name": "AliExpress",
        "key": "aliexpress",
        "url": "https://www.aliexpress.com/",
        "profile": DATA_BROWSER_DIR / "aliexpress",
    },
}

async def open_login(store_info: dict) -> None:
    profile_dir = store_info["profile"]
    profile_dir.mkdir(parents=True, exist_ok=True)
    
    # Remove stale lock files
    lock_file = profile_dir / "SingletonLock"
    if lock_file.exists():
        try:
            lock_file.unlink()
        except Exception:
            pass

    print(f"\n========================================================")
    print(f"  Oeffne Chrome fuer: {store_info['name']}")
    print(f"  URL: {store_info['url']}")
    print(f"  Profil: {profile_dir}")
    print(f"========================================================")
    print("  👉 Google Chrome oeffnet sich jetzt direkt auf deinem Bildschirm!")
    print("  👉 Logge dich ganz normal mit deinem Account ein (auch 2FA).")
    print("  👉 WICHTIG: Setze unbedingt den Haken bei 'Angemeldet bleiben' / 'Remember Me'!")
    print("========================================================\n")

    if sys.platform != "win32":
        os.environ["DISPLAY"] = ":1"

    browser_args = [
        "--ignore-gpu-blocklist",
        "--enable-unsafe-webgpu",
        "--restore-last-session",
    ]
    if sys.platform != "win32":
        browser_args.extend(["--no-sandbox", "--disable-dev-shm-usage"])

    browser = await uc.start(
        user_data_dir=str(profile_dir),
        headless=False,
        sandbox=True if sys.platform == "win32" else False,
        browser_args=browser_args,
    )

    page = await browser.get(store_info["url"])
    print(f"[{store_info['name']}] Browser ist geoeffnet.")
    print("Druecke [ENTER] hier im Terminal, sobald du mit dem Einloggen FERTIG bist...")
    
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, sys.stdin.readline)

    print(f"Speichere Session und schliesse Browser fuer {store_info['name']}...")
    try:
        await page.send(uc.cdp.browser.close())
    except Exception:
        pass
    await asyncio.sleep(2)
    try:
        browser.stop()
    except Exception:
        pass
    print(f"✔ {store_info['name']} erfolgreich gespeichert!\n")


async def main():
    target = sys.argv[1].strip().lower() if len(sys.argv) > 1 else None

    if target in STORES:
        await open_login(STORES[target])
        return

    # Check by key (e.g. "steam", "epic")
    matched = next((info for info in STORES.values() if info["key"] == target), None)
    if matched:
        await open_login(matched)
        return

    # Menu
    while True:
        print("\n========================================================")
        print("     FREE GAMES CLAIMER - STORE LOGIN ASSISTENT (PC)")
        print("========================================================")
        print("  [1] Epic Games einloggen (inkl. Fab)")
        print("  [2] Steam einloggen")
        print("  [3] GOG einloggen")
        print("  [4] Amazon / Prime Gaming einloggen")
        print("  [5] Ubisoft einloggen")
        print("  --- Optionale Stores ---")
        print("  [6] Itch.io einloggen")
        print("  [7] Fanatical einloggen")
        print("  [8] IndieGala einloggen")
        print("  [9] Unity Asset Store einloggen")
        print("  [10] AliExpress einloggen")
        print("  [q] Beenden")
        print("========================================================")
        choice = input("Waehle einen Store (1-10 oder q): ").strip()
        if choice.lower() == "q":
            print("Beende Login-Assistent.")
            break
        if choice in STORES:
            await open_login(STORES[choice])
        else:
            print("Ungueltige Auswahl.")

if __name__ == "__main__":
    asyncio.run(main())
