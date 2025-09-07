# Use a slim Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .

# Install system dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy requirements
COPY . .

# Optional port for health check
EXPOSE 8080

# Start the bot
CMD ["python", "main.py"]
