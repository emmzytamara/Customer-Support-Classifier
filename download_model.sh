#!/bin/bash

# download_model.sh - Download model from Google Drive if not present

MODEL_DIR="/app/model"
GDRIVE_FILE_ID="${GDRIVE_FILE_ID:-1t-X6C2vL94D-m4e2Thd2HDclcbaPLN47}"

if [ ! -d "$MODEL_DIR" ]; then
    echo "📥 Downloading model from Google Drive..."
    echo "File ID: $GDRIVE_FILE_ID"
    
    # Download directly without --id flag (deprecated)
    gdown --fuzzy "$GDRIVE_FILE_ID" -O /app/model.zip
    
    if [ $? -eq 0 ]; then
        echo "📦 Extracting model files..."
        
        # Extract the zip
        unzip -q /app/model.zip -d /app/temp_extract/
        
        # Find the model directory (it might be nested)
        MODEL_FOLDER=$(find /app/temp_extract -type d -name "distilbert*" | head -n 1)
        
        if [ -n "$MODEL_FOLDER" ]; then
            echo "✅ Found model at: $MODEL_FOLDER"
            mv "$MODEL_FOLDER" /app/model
            rm -rf /app/temp_extract
            rm /app/model.zip
            echo "✅ Model setup complete!"
        else
            echo "❌ Could not find model folder in extracted files"
            echo "Contents of extracted archive:"
            ls -la /app/temp_extract/
            exit 1
        fi
        
        # Verify model files
        if [ -f "/app/model/config.json" ] && [ -f "/app/model/model.safetensors" ]; then
            echo "✅ Model files verified:"
            ls -la /app/model/
        else
            echo "❌ Required model files missing!"
            ls -la /app/model/
            exit 1
        fi
    else
        echo "❌ Failed to download model from Google Drive"
        exit 1
    fi
else
    echo "✅ Model already exists at $MODEL_DIR"
fi
