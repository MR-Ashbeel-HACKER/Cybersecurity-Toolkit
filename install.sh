#!/bin/bash

# Set up the environment for the Cybersecurity Toolkit

echo "Starting installation of Cybersecurity Toolkit..."

# Update system and install dependencies
echo "Updating system packages..."
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Python 3 and pip if not already installed
echo "Installing Python 3 and pip..."
sudo apt-get install -y python3 python3-pip python3-venv

# Install essential libraries for penetration testing and network analysis
echo "Installing penetration testing and security tools..."
sudo apt-get install -y nmap metasploit-framework nikto aircrack-ng hydra john burpsuite \
    sqlmap libpcap-dev wireshark openvas nessus qualys-scan lynis \
    volatility autopsy sleuthkit ftk-imager medusa hashcat ossec splunk \
    elasticsearch logstash kibana zeek

# Install specific Python libraries for the toolkit
echo "Installing required Python libraries..."
pip3 install --upgrade pip
pip3 install nmap subprocess pyshark

# Install Volatility, if not already installed
echo "Installing Volatility (memory forensics)..."
pip3 install volatility3

# Install Metasploit if it's not already installed
echo "Installing Metasploit Framework..."
sudo apt-get install -y metasploit-framework

# Set up the necessary folders and paths
echo "Setting up directories for the toolkit..."
mkdir -p ~/cybersecurity-toolkit
cd ~/cybersecurity-toolkit

# Clone the repository with your Python toolkit (optional, if your code is on GitHub)
# echo "Cloning Cybersecurity Toolkit repository..."
# git clone https://github.com/your-repository/cybersecurity-toolkit.git

# Make the Python script executable
echo "Making the Python toolkit executable..."
chmod +x /path/to/your/python_script.py  # Replace with actual path

# Give the user an option to run the toolkit now
echo "Installation complete!"
echo "To run the toolkit, simply execute the Python script."
echo "Example: python3 /path/to/your/python_script.py"

# Add finishing message
echo "Cybersecurity Toolkit setup complete. Run the toolkit with 'python3 /path/to/your/python_script.py'."

# End of script
exit 0
