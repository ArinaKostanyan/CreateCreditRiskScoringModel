#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Install Python 3.10
install_python3_10() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "Installing Python 3.10 on Linux..."
        sudo apt update && sudo apt install -y python3.10 python3.10-venv python3.10-distutils
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "Installing Python 3.10 on macOS..."
        brew install python@3.10
    elif [[ "$OSTYPE" == "msys"* || "$OSTYPE" == "cygwin"* ]]; then
        echo "Installing Python 3.10 on Windows..."
        echo "Please download and install Python 3.10 manually from https://www.python.org/downloads/"
        echo "Ensure Python 3.10 is added to your PATH."
        exit 1
    else
        echo "Please install Python 3.10 manually. This file is not providing Python 3.10 installation for your OS, Sorry."
        exit 1
    fi
}

# Check if Python 3.10 is installed
if command_exists python3.10; then
    echo "Python 3.10 is already installed."
else
    install_python3_10
fi

# Verify Python 3.10 installation
if ! command_exists python3.10; then
    echo "Python 3.10 installation failed. Exiting."
    exit 1
fi

# Create a virtual environment using Python 3.10
echo "Setting up a virtual environment..."
python3.10 -m venv venv
source venv/bin/activate

# Upgrade pip in the virtual environment
echo "Upgrading pip..."
pip install --upgrade pip

# Install prerequisites
if [[ -f "requirements.txt" ]]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Skipping dependencies installation."
fi

# Run the main script
if [[ -f "main.py" ]]; then
    echo "Running main.py..."
    python main.py
else
    echo "main.py not found. Exiting."
    deactivate
    exit 1
fi

# Deactivate virtual environment
deactivate
echo "Script completed successfully."
