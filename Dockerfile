# Use official Python image
FROM python:3.11-slim

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system deps (for pyppeteer + chroma)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (cache optimization)
COPY requirements.txt .

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port if later API added
EXPOSE 8000

# Use official Python image
FROM python:3.11-slim

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system deps (for pyppeteer + chroma)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (cache optimization)
COPY requirements.txt .

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port if later API added
EXPOSE 8000

# Default command
CMD ["python", "app/main.py"]