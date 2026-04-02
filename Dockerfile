FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    poppler-utils \
    && apt-get clean

# Set working directory
WORKDIR /app

# Copy only requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the project
COPY . .

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]