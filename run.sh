#!/bin/bash

# Quick start script for Document Q&A Bot

set -e

echo "Setting up virtual environment..."
python -m venv venv
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Checking for .env file..."
if [ ! -f .env ]; then
    echo "No .env found. Copying from .env.example..."
    cp .env.example .env
    echo "Please add your API keys to .env before continuing."
    exit 1
fi

echo "Starting Streamlit app..."
streamlit run app/main.py