import os
import zipfile
from playwright.sync_api import sync_playwright

# 1️⃣ Zip repo contents
zip_filename = "bot.zip"
with zipfile.ZipFile(zip_filename, "w") as zipf:
    for root, dirs, files in os.walk("."):
        for file in files:
            if ".git" in root or ".github" in root:
                continue
            zipf.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file), "."))

# 2️⃣ Upload via Playwright
email = os.environ["WISPBYTE_EMAIL"]
password = os.environ["WISPBYTE_PASSWORD"]
server_url = os.environ["SERVER_URL"]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    # Go to Wispbyte login page
    page.goto("https://wispbyte.com/login")
    page.fill("input[name='email']", email)
    page.fill("input[name='password']", password)
    page.click("button[type='submit']")
    page.wait_for_load_state("networkidle")
    
    # Go to server console page
    page.goto(server_url)
    
    # Click upload button (update the selector to match Wispbyte's upload button)
    page.set_input_files("input[type='file']", zip_filename)
    
    # Wait for upload to finish (may need to adjust selector or wait time)
    page.wait_for_timeout(10000)
    
    browser.close()
