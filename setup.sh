#!/bin/bash

# Update system packages
echo "Updating system packages..."
sudo apt-get update

# Install system dependencies for Ubuntu 22.04
echo "Installing system dependencies..."
sudo apt-get install -y python3-tk

# Install Python dependencies
echo "Installing Python dependencies from requirements.txt..."
pip install -r requirements.txt

# Download additional data for textblob
echo "Downloading necessary corpora for textblob..."
python3 -m textblob.download_corpora

echo "Setup completed successfully!"
