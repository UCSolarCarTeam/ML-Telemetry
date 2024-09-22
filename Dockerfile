# Use the official Python base image
FROM python:3.9-slim

# Set environment variables to prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a working directory
WORKDIR /app

# Copy requirements.txt if you have one, otherwise install dependencies directly in the Dockerfile
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# If you have application code, copy it to the working directory
COPY ./app .

# Set the default command to run your application
# CMD ["python", "your_script.py"]

# Example: Run an interactive shell by default
CMD ["bash"]
