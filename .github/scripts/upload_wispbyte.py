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
server_url = os.environ["WISPBYTE_SERVER_URL"]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Go to Wispbyte login page
    page.goto("https://wispbyte.com/client/login")
    page.fill("input[name='Email or Username']", email)
    page.fill("input[name='Password']", password)
    page.click("button[type='Log In']")
    page.wait_for_load_state("networkidle")
    
    # Go to server files page
    page.goto(server_url)
    
    page.wait_for_selector("text=Upload")
    page.click("text=Upload")

    page.wait_for_selector("text=upload manually")
    page.click("text=upload manually")

    page.set_input_files("input[type='file']", zip_filename)
    
    # Wait for upload to finish (may need to adjust selector or wait time)
    page.wait_for_timeout(10000)

    print("Upload complete!")

    browser.close()
