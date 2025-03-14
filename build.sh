#!/bin/bash
set -e

# Install required dependencies for ChromeDriver
apt-get update && apt-get install -y wget unzip libnss3 libxss1 libappindicator3-1 fonts-liberation

# Ensure chromedriver is available
mkdir -p /app/chromedriver
wget -q https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
unzip -o chromedriver_linux64.zip -d /app/chromedriver
chmod +x /app/chromedriver/chromedriver

echo "[INFO] Build script completed successfully."
