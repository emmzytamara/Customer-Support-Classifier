# -------------------------------
# Base Image
# -------------------------------
FROM python:3.10

# -------------------------------
# Set Working Directory
# -------------------------------
WORKDIR /app

# -------------------------------
# Install system dependencies
# -------------------------------
RUN apt-get update && apt-get install -y \
    unzip \
    curl \
    && rm -rf /var/lib/apt/lists/*

# -------------------------------
# Install gdown for Google Drive downloads
# -------------------------------
RUN pip install --no-cache-dir gdown

# -------------------------------
# Copy Requirements
# -------------------------------
COPY requirements.txt .

# -------------------------------
# Install Dependencies
# -------------------------------
RUN pip install --no-cache-dir -r requirements.txt

# -------------------------------
# Copy Application Files
# -------------------------------
COPY app.py /app/app.py
COPY download_model.sh /app/download_model.sh

# Copy UI files
COPY ui/index.html /app/static/index.html

# Make download script executable
RUN chmod +x /app/download_model.sh

# Create MLflow tracking directory
RUN mkdir -p /app/mlruns

# -------------------------------
# Environment Variables
# -------------------------------
ENV PORT=7860

# -------------------------------
# Expose API Port (HF Spaces uses 7860 by default)
# -------------------------------
EXPOSE 7860

# -------------------------------
# Healthcheck
# -------------------------------
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
  CMD curl -f http://localhost:7860/health || exit 1

# -------------------------------
# Run Application
# Download model at startup, then start server
# -------------------------------
CMD ["/bin/bash", "-c", "/app/download_model.sh && uvicorn app:app --host 0.0.0.0 --port 7860"]
