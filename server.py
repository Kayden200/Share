
import os
import undetected_chromedriver as uc

# Use /tmp instead of /app (Render does not allow writing to /app)
CHROMEDRIVER_DIR = "/tmp/chromedriver"
CHROMEDRIVER_PATH = f"{CHROMEDRIVER_DIR}/chromedriver"
CHROME_BINARY_PATH = "/usr/bin/google-chrome-stable"  # Manually set Chrome binary location

# Ensure the directory exists before extracting
if not os.path.exists(CHROMEDRIVER_DIR):
    os.makedirs(CHROMEDRIVER_DIR, exist_ok=True)

# Download ChromeDriver if it doesn’t exist
if not os.path.exists(CHROMEDRIVER_PATH):
    print("[INFO] Downloading ChromeDriver...")
    os.system("wget -q https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip")
    os.system(f"unzip -o chromedriver_linux64.zip -d {CHROMEDRIVER_DIR}")
    os.system(f"chmod +x {CHROMEDRIVER_PATH}")

# Start Chrome with the correct binary path
options = uc.ChromeOptions()
options.binary_location = CHROME_BINARY_PATH  # Explicitly set Chrome's binary location
options.add_argument("--headless")
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
