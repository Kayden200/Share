#!/bin/bash
set -e

# Install missing dependencies for ChromeDriver
apt-get update && apt-get install -y libnss3 libxss1 libappindicator3-1 fonts-liberation

# Ensure chromedriver is in the right place
mkdir -p /app/chromedriver
unzip -o chromedriver_linux64.zip -d /app/chromedriver
chmod +x /app/chromedriver/chromedriver
