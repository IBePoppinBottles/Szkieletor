import os
import shutil
import zipfile
from pathlib import Path
from playwright.sync_api import sync_playwright


EMAIL = os.environ.get("WISPBYTE_EMAIL")
PASSWORD = os.environ.get("WISPBYTE_PASSWORD")
SERVER_URL = os.environ.get("WISPBYTE_SERVER_URL")

ZIP_FILE = "bot.zip"


def create_zip():
    """Create a fresh ZIP of the repo (excluding .git and the zip itself)."""
    if Path(ZIP_FILE).exists():
        os.remove(ZIP_FILE)

    with zipfile.ZipFile(ZIP_FILE, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk("."):
            if ".git" in dirs:
                dirs.remove(".git")  # skip .git folder
            for file in files:
                if file == ZIP_FILE:
                    continue
                filepath = Path(root) / file
                zf.write(filepath, filepath.relative_to("."))

    print(f"[INFO] Created {ZIP_FILE}")


def upload_zip():
    print("[DEBUG] Launching browser...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("[DEBUG] Logging into Wispbyte...")
        page.goto("https://wispbyte.com/client/login")
        page.fill('input[name="email"]', EMAIL)
        page.fill('input[name="password"]', PASSWORD)
        page.click('button[type="submit"]')
        page.wait_for_selector("text=Szkieletor", timeout=60000)
        print("[DEBUG] Logged in successfully!")
        
        page.goto(SERVER_URL)
        page.wait_for_load_state("networkidle")
    
        print("[DEBUG] Clicking upload buttons...")
        page.click("button:has-text('Upload')")
        page.click("button:has-text('upload manually')")

        
        print("[DEBUG] Selecting file...")
        with page.expect_file_chooser() as fc_info:
            page.click("input[type='file']")
        file_chooser = fc_info.value
        file_chooser.set_files(ZIP_FILE)
        print(f"[INFO] Uploaded {ZIP_FILE} to Wispbyte.")

        print("[DEBUG] Upload complete!")
        browser.close()


if __name__ == "__main__":
    if not EMAIL or not PASSWORD or not SERVER_URL:
        raise ValueError("Missing environment variables: WISPBYTE_EMAIL, WISPBYTE_PASSWORD, WISPBYTE_SERVER_URL")

    create_zip()
    upload_zip()
