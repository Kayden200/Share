import os
import undetected_chromedriver as uc

# Define ChromeDriver path inside the Render environment
CHROMEDRIVER_PATH = "/app/chromedriver/chromedriver"

# Ensure chromedriver is downloaded
if not os.path.exists(CHROMEDRIVER_PATH):
    print("[INFO] Downloading ChromeDriver...")
    os.system("wget -q https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip")
    os.system("unzip -o chromedriver_linux64.zip -d /app/chromedriver")
    os.system("chmod +x /app/chromedriver/chromedriver")

# Start Chrome with custom driver path
options = uc.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

print("[INFO] Starting ChromeDriver...")
driver = uc.Chrome(driver_executable_path=CHROMEDRIVER_PATH, options=options)

try:
    driver.get("https://www.facebook.com/")
    print("[INFO] Successfully loaded Facebook")
finally:
    driver.quit()
    print("[INFO] ChromeDriver closed.")
