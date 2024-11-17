## Full Installation Guide for Cybersecurity Toolkit

### Introduction:
This script is a comprehensive cybersecurity toolkit that integrates multiple tools for penetration testing, forensics, brute-forcing, threat hunting, and security auditing. The script allows you to automate tasks such as running Nmap scans, cracking passwords, running Metasploit exploits, launching Burp Suite, and using various forensics tools.

### System Requirements:
To run this script, you'll need:
- A Linux-based OS (preferred for cybersecurity tools), such as Ubuntu, Kali Linux, or Debian.
- Python 3.x installed (Python 3.6 or higher).
- Root or sudo privileges to install certain tools.

### Step-by-Step Installation:

1. **Install Python 3 and Required Libraries:**
   First, ensure Python 3 and `pip` (Python's package installer) are installed. You can install them with:

   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```

2. **Install Python Dependencies:**
   The script uses several Python libraries, which you can install via `pip`. Run the following command to install them:

   ```bash
   pip3 install nmap requests paramiko termcolor pyfiglet pyshark scapy
   ```

   **Explanation:**
   - `nmap`: For interacting with the Nmap port scanner.
   - `requests`: For making HTTP requests.
   - `paramiko`: For SSH functionality.
   - `termcolor`: For colored terminal output.
   - `pyfiglet`: For ASCII art banners.
   - `pyshark`: For packet analysis using Wireshark.
   - `scapy`: For network packet manipulation.

3. **Install Additional Tools:**
   The toolkit relies on several external penetration testing and forensics tools, which you need to install separately. Here’s how to install them:

   - **Nmap:**
     ```bash
     sudo apt install nmap
     ```

   - **Metasploit Framework:**
     Follow the official installation guide for Metasploit on Ubuntu:
     [Metasploit Installation Guide](https://docs.metasploit.com/docs/using-metasploit/installation/ubuntu.html)

     Or simply use:
     ```bash
     sudo apt install metasploit-framework
     ```

   - **Burp Suite:**
     You can download Burp Suite from its official website:
     [Burp Suite Download](https://portswigger.net/burp/communitydownload)
     After downloading, follow the installation instructions on the website.

   - **Aircrack-ng:**
     ```bash
     sudo apt install aircrack-ng
     ```

   - **Nikto:**
     ```bash
     sudo apt install nikto
     ```

   - **Hydra:**
     ```bash
     sudo apt install hydra
     ```

   - **Volatility (for Memory Analysis):**
     ```bash
     sudo apt install volatility
     ```

   - **FTK Imager:**
     FTK Imager is a Windows-based tool, so you will need to run it on a Windows machine or use a compatibility layer like Wine. Download it from the official site:
     [FTK Imager Download](https://accessdata.com/product-download/ftk-imager)

   - **Autopsy:**
     ```bash
     sudo apt install autopsy
     ```

   - **The Sleuth Kit:**
     ```bash
     sudo apt install sleuthkit
     ```

   - **John the Ripper:**
     ```bash
     sudo apt install john
     ```

   - **Hashcat:**
     ```bash
     sudo apt install hashcat
     ```

   - **Medusa:**
     ```bash
     sudo apt install medusa
     ```

   - **Splunk:**
     Download and install Splunk from the official website:
     [Splunk Download](https://www.splunk.com/en_us/download.html)

   - **OSSEC:**
     ```bash
     sudo apt install ossec-hids
     ```

   - **Zeek:**
     ```bash
     sudo apt install zeek
     ```

   - **Lynis:**
     ```bash
     sudo apt install lynis
     ```

   - **OpenVAS:**
     ```bash
     sudo apt install openvas
     ```

   - **Nessus:**
     You can download Nessus from the official website:
     [Nessus Download](https://www.tenable.com/products/nessus)

   - **Qualys:**
     You need to sign up for the Qualys Cloud Agent. After registration, download the agent from the website and follow the installation instructions:
     [Qualys Download](https://www.qualys.com/)

4. **Create a Virtual Environment (optional but recommended):**
   To avoid conflicts with system packages, you may want to create a virtual environment for this project:

   ```bash
   python3 -m venv cybersecurity_env
   source cybersecurity_env/bin/activate
   ```

   Install the dependencies in this environment using `pip` as shown earlier.

5. **Setting Up the Toolkit:**
   Download the Python script and save it to your local machine. For example, save it as `cyber_toolkit.py`.

   If you are running this on Kali Linux or a similar penetration testing system, ensure that all the tools installed above are accessible in your `$PATH`.

6. **Running the Toolkit:**
   Once all dependencies and tools are installed, run the script with the following command:

   ```bash
   python3 cyber_toolkit.py
   ```

   This will launch the main menu, and you can choose which tools to run interactively.

7. **Permissions and Access:**
   Some tools, such as `nmap`, `metasploit`, and `hydra`, require root privileges to function properly. Ensure that you have the appropriate permissions or run the script with `sudo` if needed.

   For example:

   ```bash
   sudo python3 cyber_toolkit.py
   ```

### Troubleshooting:

- **Missing Dependencies:**
  If any of the tools or libraries fail to run, check that they are installed correctly and accessible via your terminal. You can test individual tools by running them from the command line to verify installation.

- **Permissions Errors:**
  Some tools might require root permissions to execute correctly (e.g., Metasploit, Nmap, Aircrack-ng). Use `sudo` to run the toolkit if necessary.

### Final Notes:
- Always use cybersecurity tools ethically and legally. Make sure you have explicit permission to perform penetration tests on any network or system.
- Stay up to date with tool versions and security patches for the software you're using.

Enjoy exploring the Cybersecurity Toolkit and improving your penetration testing and forensics skills!
