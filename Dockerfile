# Python base image
FROM python:3.12-slim

# Working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port (Render ke liye)
EXPOSE 10000

# Start bot
CMD ["python", "bot.py"]
