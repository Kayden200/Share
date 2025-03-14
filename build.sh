#!/bin/bash
set -e

# Install dependencies for Chrome
apt-get update && apt-get install -y wget unzip curl libnss3 libxss1 libappindicator3-1 fonts-liberation

# Download & Install Google Chrome
echo "[INFO] Installing Google Chrome..."
wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i google-chrome-stable_current_amd64.deb || apt-get install -fy

# Ensure ChromeDriver is available
mkdir -p /tmp/chromedriver
wget -q https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
unzip -o chromedriver_linux64.zip -d /tmp/chromedriver
chmod +x /tmp/chromedriver/chromedriver

echo "[INFO] Build script completed successfully."
