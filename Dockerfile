# Use a Python base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install dependencies required for various tools
RUN apt-get update && apt-get install -y \
    nmap \
    metasploit-framework \
    burpsuite \
    aircrack-ng \
    nikto \
    hydra \
    volatility \
    ftkimager \
    autopsy \
    sleuthkit \
    john \
    hashcat \
    medusa \
    splunk \
    ossec-hids \
    zeek \
    lynis \
    openvas \
    nessus \
    qualys-cloud-agent \
    git \
    curl \
    && apt-get clean

# Install Python dependencies (if any)
# If the script has any dependencies listed in requirements.txt, you can uncomment the next two lines
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# Copy the Python script into the container
COPY test.py /app/test.py


# If Burp Suite is installed and needs to be accessed via the web interface, expose the port
# For Burp Suite, we would typically expose 8080 if you're running its web proxy
# EXPOSE 8080  # Uncomment this if you plan to use Burp Suite's web interface

# Set the default command to run the Python script
CMD ["python", "app.py"]
