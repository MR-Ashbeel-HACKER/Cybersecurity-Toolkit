Cybersecurity Toolkit
The Cybersecurity Toolkit is a collection of tools designed for penetration testing, forensic analysis, vulnerability scanning, and other cybersecurity tasks. This toolkit integrates various security tools such as Nmap, Metasploit, Burp Suite, Hydra, John the Ripper, and more into one easy-to-use interface.

This README.md file provides detailed instructions on how to install, configure, and run the toolkit on your system or via Docker.

Table of Contents
Introduction
Installation
Linux Installation
Using the install.sh Script
Docker Installation
Docker Compose Installation
Running the Toolkit
Troubleshooting
License
Introduction
The Cybersecurity Toolkit allows you to run various cybersecurity tools directly from a single interface. It supports several types of operations, including:

Penetration Testing (Nmap, Metasploit, Hydra, Burp Suite)
Forensics (Volatility, FTK Imager, Autopsy)
Brute-Forcing (John the Ripper, Hashcat, Medusa)
Security Auditing (Lynis, OpenVAS, Nessus, Qualys)
Threat Hunting (Splunk, Zeek, OSSEC)
Installation
You can install the Cybersecurity Toolkit either directly on your Linux-based system or inside a Docker container. Below are the steps for both methods.

Linux Installation
Follow these steps to install the Cybersecurity Toolkit on a Linux system.

1. Install System Dependencies
First, ensure your system is up-to-date and has all the necessary dependencies for the toolkit.

bash
Copy code
# Update and upgrade system packages
sudo apt update && sudo apt upgrade -y

# Install Python and required libraries
sudo apt install -y python3 python3-pip python3-venv build-essential git curl

# Install necessary security tools
sudo apt install -y nmap metasploit-framework burpsuite hydra aircrack-ng nikto john hashcat medusa splunk ossec zeek lynis openvas nessus
2. Install Python Dependencies
You can install Python dependencies using the requirements.txt file. Here's how:

bash
Copy code
# Clone the repository
git clone https://github.com/your-repository/cybersecurity_toolkit.git
cd cybersecurity_toolkit

# Create a Python virtual environment and activate it
python3 -m venv env
source env/bin/activate

# Install Python dependencies
pip install -r requirements.txt
Using the install.sh Script
If you want to automate the installation process, you can use the install.sh script. This will install all dependencies, including system tools and Python libraries.

1. Make the install.sh Script Executable
bash
Copy code
chmod +x install.sh
2. Run the Script
bash
Copy code
./install.sh
This script will automatically handle the installation of the required tools and dependencies.

Docker Installation
If you prefer using Docker to run the toolkit, follow these steps:

1. Install Docker
Follow the installation instructions for Docker on your system:

Install Docker
Install Docker Compose
Once Docker is installed, verify it by running:

bash
Copy code
docker --version
docker-compose --version
2. Build and Run the Docker Image
Clone the repository:

bash
Copy code
git clone https://github.com/your-repository/cybersecurity_toolkit.git
cd cybersecurity_toolkit
Build the Docker Image:

bash
Copy code
docker build -t cybersecurity_toolkit .
Run the Docker Container:

Once the image is built, you can run the toolkit in a container:

bash
Copy code
docker run -it cybersecurity_toolkit
This command will run the Cybersecurity Toolkit inside a Docker container.

Docker Compose Installation
For even easier setup, you can use Docker Compose, which simplifies multi-container Docker applications.

1. Install Docker Compose
Follow the official guide to install Docker Compose on your system.

2. Build and Start the Docker Containers
Clone the repository:

bash
Copy code
git clone https://github.com/your-repository/cybersecurity_toolkit.git
cd cybersecurity_toolkit
Build and Start the Docker Containers:

bash
Copy code
docker-compose up --build
Access the Running Container:

You can access the running container by executing:

bash
Copy code
docker exec -it cybersecurity_toolkit /bin/bash
Running the Toolkit
Once you've installed the Cybersecurity Toolkit, you can begin using it immediately.

Activate the Virtual Environment (if not using Docker):

If you installed the toolkit locally, you may want to activate the Python virtual environment:

bash
Copy code
source env/bin/activate
Run the Toolkit:

You can start the toolkit by running the following command:

bash
Copy code
python3 main.py
Main Menu:

After running the above command, you'll be presented with a menu of available tools:

mathematica
Copy code
Cybersecurity Toolkit
1. Run Nmap Scan
2. Run Metasploit Exploit
3. Launch Burp Suite
4. Crack Wi-Fi with Aircrack-ng
5. Run Nikto Web Scan
6. Run Hydra Brute Force
7. Run John the Ripper
8. Analyze Memory with Volatility
9. Launch FTK Imager
10. Launch Autopsy
11. Analyze with Sleuth Kit
12. Run Hashcat
13. Run Medusa Brute Force
14. Run Splunk Search
15. Run OSSEC
16. Start Zeek
17. Run Lynis Security Audit
18. Run OpenVAS Scan
19. Run Nessus Scan
20. Run Qualys Scan
21. Exit
To select a tool, just type the number associated with it.

Troubleshooting
If you encounter any issues, here are some common solutions:

Permission Denied for install.sh: If you get a "Permission Denied" error when trying to run the install.sh script, make it executable:

bash
Copy code
chmod +x install.sh
Missing Dependencies: If a tool is missing, manually install it using apt:

bash
Copy code
sudo apt install <missing-tool>
Docker Issues: If Docker containers aren't running, ensure that Docker and Docker Compose are correctly installed:

bash
Copy code
docker --version
docker-compose --version
Restart Docker:

bash
Copy code
sudo systemctl restart docker
