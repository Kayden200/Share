from flask import Flask, request, jsonify, render_template
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)

# Set up Chrome options for Termux
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Run without opening a browser
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Specify Chromedriver path in Termux
service = Service("/data/data/com.termux/files/usr/bin/chromedriver")

@app.route('/')
def index():
    return render_template('spamshare.html')  # Load your frontend

@app.route('/share', methods=['POST'])
def share():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    post_link = data.get('post_link')
    share_count = int(data.get('share_count', 1))

    if not all([email, password, post_link]):
        return jsonify({"error": "Missing required fields"}), 400

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://m.facebook.com")

    # Login
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "m_login_email"))).send_keys(email)
    driver.find_element(By.ID, "m_login_password").send_keys(password)
    driver.find_element(By.NAME, "login").click()

    # Verify login success
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'logout')]")))
        print(f"[✅] Logged in: {email}")
    except:
        print(f"[❌] Login failed: {email}")
        driver.quit()
        return jsonify({"error": "Login failed"}), 401

    # Start Sharing
    for i in range(share_count):
        print(f"[🔄] {email} - Sharing {i+1}/{share_count}...")

        driver.get(f"https://m.facebook.com/sharer.php?u={post_link}")

        try:
            post_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(text(), 'Post')]"))
            )
            post_button.click()
            print(f"[✅] {email} - Shared {i+1}/{share_count} successfully!")
        except:
            print(f"[❌] {email} - Failed to share {i+1}/{share_count}")

        time.sleep(random.randint(5, 10))

    driver.quit()
    return jsonify({"success": f"Post shared {share_count} times!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
