# Use a lightweight Python image
FROM python:3.11-slim

# Install required dependencies
RUN apt update && apt install -y \
    wget unzip curl \
    chromium chromium-driver

# Set environment variables for Chrome
ENV DISPLAY=:99
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . /app

# Expose the port your app runs on (update if needed)
EXPOSE 8000

# Run the application
CMD ["python", "server.py"]
