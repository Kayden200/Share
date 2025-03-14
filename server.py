import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set paths
CHROMEDRIVER_PATH = "/tmp/chromedriver/chromedriver"
CHROME_BINARY_PATH = "/usr/bin/google-chrome"  # Adjusted Chrome binary path
# Ensure ChromeDriver exists
if not os.path.exists(CHROMEDRIVER_PATH):
    print("[INFO] Downloading ChromeDriver...")
    os.system("wget -q https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip")
    os.system("unzip -o chromedriver_linux64.zip -d /tmp/chromedriver")
    os.system("chmod +x /tmp/chromedriver/chromedriver")

# Configure Chrome options
options = Options()
options.binary_location = CHROME_BINARY_PATH  # Set Chrome binary location
options.add_argument("--headless")  # Run headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Start ChromeDriver using Selenium
print("[INFO] Starting ChromeDriver...")
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://www.facebook.com/")
    print("[INFO] Successfully loaded Facebook")
finally:
    driver.quit()
    print("[INFO] ChromeDriver closed.")
