import os
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

# 🔹 Install Chrome & Chromedriver in Render if missing
chrome_bin = "/usr/bin/google-chrome"
chrome_driver = "/usr/bin/chromedriver"

if not os.path.exists(chrome_bin) or not os.path.exists(chrome_driver):
    print("[🔄] Installing Google Chrome & Chromedriver...")
    subprocess.run("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb", shell=True)
    subprocess.run("apt install -y ./google-chrome-stable_current_amd64.deb", shell=True)
    subprocess.run("wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip", shell=True)
    subprocess.run("unzip chromedriver_linux64.zip", shell=True)
    subprocess.run("mv chromedriver /usr/bin/chromedriver", shell=True)
    subprocess.run("chmod +x /usr/bin/chromedriver", shell=True)

# 🔹 Configure Headless Chrome for Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Run without GUI
chrome_options.add_argument("--no-sandbox")  # Required for Render
chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent memory issues
chrome_options.add_argument("--disable-gpu")

# 🔹 Example Selenium Function: Open Facebook
def test_facebook():
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://m.facebook.com")
    print("[✅] Opened Facebook Successfully!")
    driver.quit()

@app.route('/')
def index():
    return render_template('spamshare.html')

if __name__ == '__main__':
    test_facebook()  # Test Chrome setup
    port = int(os.environ.get("PORT", 5000))  # Get Render's dynamic port
    app.run(host='0.0.0.0', port=port, debug=False)
