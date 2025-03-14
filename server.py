import os
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

# ✅ Step 1: Install Chrome & Chromedriver in Render's Temp Directory
CHROME_BIN = "/usr/bin/google-chrome"
CHROMEDRIVER_BIN = "/usr/local/bin/chromedriver"

if not os.path.exists(CHROMEDRIVER_BIN):
    print("[🔄] Installing Chrome & Chromedriver on Render...")

    subprocess.run("wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb", shell=True)
    subprocess.run("apt install -y ./google-chrome-stable_current_amd64.deb", shell=True)
    subprocess.run("wget -q https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip", shell=True)
    subprocess.run("unzip chromedriver_linux64.zip -d /usr/local/bin/", shell=True)
    subprocess.run("chmod +x /usr/local/bin/chromedriver", shell=True)

# ✅ Step 2: Configure Chrome & Chromedriver for Headless Mode
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = CHROME_BIN
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")  # Required for Render
chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent memory issues
chrome_options.add_argument("--disable-gpu")

# ✅ Step 3: Test Chrome in Render
def test_facebook():
    service = Service(CHROMEDRIVER_BIN)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://m.facebook.com")
    print("[✅] Opened Facebook Successfully!")
    driver.quit()

@app.route('/')
def index():
    return render_template('spamshare.html')

if __name__ == '__main__':
    test_facebook()  # Test Chrome setup on Render
    port = int(os.environ.get("PORT", 5000))  # Use Render's dynamic port
    app.run(host='0.0.0.0', port=port, debug=False)
