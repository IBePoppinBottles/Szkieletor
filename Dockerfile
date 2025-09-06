<<<<<<< HEAD
# Use a slim Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
=======
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y build-essential libjpeg-dev zlib1g-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
>>>>>>> f6b1b7c (Update GitHub Actions workflow for Fly deploy)
RUN pip install -r requirements.txt

# Copy bot code
COPY . .

<<<<<<< HEAD
# Run the bot
CMD ["python3", "main.py"]
=======
# Optional port for health check
EXPOSE 8080

CMD ["python", "main.py"]
>>>>>>> f6b1b7c (Update GitHub Actions workflow for Fly deploy)
