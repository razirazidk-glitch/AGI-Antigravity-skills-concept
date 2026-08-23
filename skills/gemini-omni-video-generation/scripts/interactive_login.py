r"""
Interactive Google Login Helper for Gemini Automation Profile
Keeps the visible Chrome window open until the user explicitly logs in and presses Enter in the terminal.
"""

import os
import sys
import asyncio
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

async def main():
    from playwright.async_api import async_playwright

    user_home = Path(os.environ.get("USERPROFILE", r"C:\Users\pichau"))
    automation_profile = user_home / ".gemini" / "chrome_automation_profile"
    automation_profile.mkdir(parents=True, exist_ok=True)

    print(f"🚀 [Login Helper] Opening Chrome browser...")
    print(f"📁 Automation Profile: {automation_profile}")

    async with async_playwright() as p:
        context = await p.chromium.launch_persistent_context(
            user_data_dir=str(automation_profile),
            channel="chrome",
            headless=False,
            viewport={"width": 1280, "height": 800},
            args=["--disable-blink-features=AutomationControlled"]
        )

        page = context.pages[0] if context.pages else await context.new_page()
        await page.goto("https://gemini.google.com/app", wait_until="domcontentloaded")

        print("\n" + "="*70)
        print("👉 THE GOOGLE CHROME WINDOW IS OPEN.")
        print("👉 Click 'Sign in' on screen and log in with your Google account.")
        print("👉 Once logged into Gemini, press ENTER HERE in the terminal.")
        print("="*70 + "\n")

        # Run input in executor to not block asyncio event loop
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, input, "⌨️  Press [ENTER] once you have completed login: ")

        print("\n💾 [Login Helper] Recording cookies and session permanently...")
        await page.screenshot(path=str(automation_profile / "logged_in_state.png"))
        await asyncio.sleep(2)
        await context.close()
        print("🎉 [Login Helper] Session saved successfully! The agent can now generate videos in the background.")

if __name__ == "__main__":
    asyncio.run(main())
