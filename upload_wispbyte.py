import os
import time
import requests
from pathlib import Path
from playwright.sync_api import sync_playwright

# -------- CONFIG --------
GITHUB_USER = "IBePoppinBottles"
GITHUB_REPO = "Szkieletor"
BRANCH = "main" 

WISPBYTE_EMAIL = os.getenv("WISPBYTE_EMAIL")
WISPBYTE_PASSWORD = os.getenv("WISPBYTE_PASSWORD")
WISPBYTE_SERVER_URL = os.getenv("WISPBYTE_SERVER_URL")

ZIP_NAME = "repo_latest.zip"
# -------------------------

def download_github_zip():
    """Download a fresh repo zip from GitHub"""
    url = f"https://github.com/{GITHUB_USER}/{GITHUB_REPO}/archive/refs/heads/{BRANCH}.zip"
    print(f"[+] Downloading {url}")
    r = requests.get(url, stream=True)
    r.raise_for_status()
    with open(ZIP_NAME, "wb") as f:
        f.write(r.content)
    print(f"[+] Saved as {ZIP_NAME}")

def upload_to_wispbyte():
    """Upload ZIP to Wispbyte using Playwright (without deploying)"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # headless for CI
        page = browser.new_page()

        # Login
        page.goto("https://wispbyte.com/login")
        page.fill("input[type='email']", WISPBYTE_EMAIL)
        page.fill("input[type='password']", WISPBYTE_PASSWORD)
        page.press("input[type='password']", "Enter")
        page.wait_for_load_state("networkidle")

        # Go to server page
        page.goto(WISPBYTE_SERVER_URL)
        page.wait_for_load_state("networkidle")

        # Upload ZIP
        file_input = page.query_selector("input[type='file']")
        if not file_input:
            raise Exception("Could not find file input — update selector")
        file_input.set_input_files(str(Path(ZIP_NAME).absolute()))
        time.sleep(2)  # optional wait to ensure upload

        print("[+] ZIP uploaded to Wispbyte (deploy not triggered)")
        browser.close()

if __name__ == "__main__":
    download_github_zip()
    upload_to_wispbyte()
