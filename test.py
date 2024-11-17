import subprocess
import nmap  # Import python-nmap for Nmap functionality
import requests
import paramiko
import logging
from termcolor import colored
import pyfiglet
import pyshark
import scapy.all as scapy

# Set up logging
logging.basicConfig(filename='cybersecurity_toolkit.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Display header with pyfiglet
def print_header():
    ascii_banner = pyfiglet.figlet_format("Cyber Toolkit")
    print(colored(ascii_banner, 'cyan'))
    print(colored("Remember Cybersecurity Toolkit  is an powerfull ToolKit so use it at your own risk \n Develop By AshbeelZai ", 'yellow'))

# ===================================================================
# 1. Penetration Testing Tools
def run_nmap_scan(target_ip):
    print(f"Running Nmap scan on {target_ip}...")
    nm = nmap.PortScanner()
    try:
        nm.scan(target_ip, arguments='-sS -sV -T4 -A')
        for host in nm.all_hosts():
            print(f"Host: {host}")
            print(f"Status: {nm[host].state()}")
            for proto in nm[host].all_protocols():
                lport = nm[host][proto].keys()
                for port in lport:
                    print(f"Port {port}: {nm[host][proto][port]['name']} ({nm[host][proto][port]['state']})")
    except Exception as e:
        print(f"Error running Nmap scan: {e}")

def run_metasploit(target_ip, exploit_name):
    print(f"Running Metasploit exploit against {target_ip} using {exploit_name}...")
    try:
        subprocess.run(f"msfconsole -q -x 'use {exploit_name}; set RHOST {target_ip}; run'", shell=True, check=True)
    except subprocess.CalledProcessError:
        print("Error running Metasploit exploit.")

def run_burp_suite():
    print("Launching Burp Suite...")
    try:
        subprocess.run("burpsuite", check=True)
    except subprocess.CalledProcessError:
        print("Error launching Burp Suite.")

def run_aircrack(interface, capture_file):
    print(f"Cracking Wi-Fi password on {interface} using capture file {capture_file}...")
    try:
        subprocess.run(f"aircrack-ng {capture_file} -w /path/to/wordlist.txt", check=True)
    except subprocess.CalledProcessError:
        print("Error running Aircrack-ng.")

def run_nikto(target_ip):
    print(f"Running Nikto scan on {target_ip}...")
    try:
        subprocess.run(f"nikto -h {target_ip}", check=True, shell=True)
    except subprocess.CalledProcessError:
        print("Error running Nikto scan.")

def run_hydra(target_ip, username, wordlist_path="/path/to/wordlist.txt"):
    print(f"Running brute-force attack on {target_ip} using Hydra...")
    try:
        subprocess.run(f"hydra -l {username} -P {wordlist_path} ssh://{target_ip}", check=True, shell=True)
    except subprocess.CalledProcessError:
        print("Error running Hydra brute force test.")

# ===================================================================
# 2. Forensics Tools
def analyze_memory(dump_path):
    print("Running memory analysis with Volatility...")
    try:
        subprocess.run(f"volatility -f {dump_path} --profile=WinXPSP2x86 pslist", shell=True, check=True)
    except subprocess.CalledProcessError:
        print("Error running memory analysis with Volatility.")

def run_ftk_imager():
    print("Launching FTK Imager...")
    try:
        subprocess.run("ftkimager", check=True)
    except subprocess.CalledProcessError:
        print("Error launching FTK Imager.")

def run_autopsy():
    print("Launching Autopsy...")
    try:
        subprocess.run("autopsy", check=True)
    except subprocess.CalledProcessError:
        print("Error launching Autopsy.")

def analyze_with_sleuth_kit():
    print("Running Sleuth Kit for disk image analysis...")
    try:
        subprocess.run("tsk_recover /path/to/disk_image", check=True, shell=True)
    except subprocess.CalledProcessError:
        print("Error using Sleuth Kit.")

# ===================================================================
# 3. Brute-Forcing Tools
def run_john_the_ripper(password_hash_file):
    print(f"Running John the Ripper on {password_hash_file}...")
    try:
        subprocess.run(f"john {password_hash_file}", check=True, shell=True)
    except subprocess.CalledProcessError:
        print("Error running John the Ripper.")

def run_hashcat(password_hash_file):
    print(f"Running Hashcat on {password_hash_file}...")
    try:
        subprocess.run(f"hashcat {password_hash_file}", check=True, shell=True)
    except subprocess.CalledProcessError:
        print("Error running Hashcat.")

def run_medusa(target_ip, username):
    print(f"Running Medusa brute-force attack on {target_ip}...")
    try:
        subprocess.run(f"medusa -h {target_ip} -u {username} -P /path/to/wordlist.txt -M ssh", check=True, shell=True)
    except subprocess.CalledProcessError:
        print("Error running Medusa.")

# ===================================================================
# 4. Threat Hunting Tools
def run_splunk_search(query):
    print(f"Running Splunk search query: {query}...")
    try:
        subprocess.run(f"splunk search '{query}'", check=True)
    except subprocess.CalledProcessError:
        print("Error running Splunk search.")

def run_ossec():
    print("Running OSSEC for HIDS...")
    try:
        subprocess.run("ossec-control start", check=True)
    except subprocess.CalledProcessError:
        print("Error starting OSSEC.")

def start_zeek():
    print("Starting Zeek network monitoring...")
    try:
        subprocess.run("zeek -i eth0", check=True)
    except subprocess.CalledProcessError:
        print("Error running Zeek.")

# ===================================================================
# 5. Security Audit Tools
def run_lynis():
    print("Running Lynis security audit...")
    try:
        subprocess.run("lynis audit system", check=True)
    except subprocess.CalledProcessError:
        print("Error running Lynis audit.")

def run_openvas_scan(target_ip):
    print(f"Running OpenVAS scan on {target_ip}...")
    try:
        subprocess.run(f"openvas-nvt-sync", check=True)
        subprocess.run(f"openvas-check-setup --status", check=True)
        subprocess.run(f"openvas -s {target_ip}", check=True)
    except subprocess.CalledProcessError:
        print("Error running OpenVAS scan.")

def run_nessus_scan(target_ip):
    print(f"Running Nessus scan on {target_ip}...")
    try:
        subprocess.run(f"nessus -q -p {target_ip}", check=True)
    except subprocess.CalledProcessError:
        print("Error running Nessus scan.")

def run_qualys_scan(target_ip):
    print(f"Running Qualys scan on {target_ip}...")
    try:
        subprocess.run(f"qualys-cloud-agent scan {target_ip}", check=True)
    except subprocess.CalledProcessError:
        print("Error running Qualys scan.")

# ===================================================================
# Main Menu Loop
def main():
    print_header()

    while True:
        print("\nCybersecurity Toolkit")
        print("1. Run Nmap Scan")
        print("2. Run Metasploit Exploit")
        print("3. Launch Burp Suite")
        print("4. Crack Wi-Fi with Aircrack-ng")
        print("5. Run Nikto Web Scan")
        print("6. Run Hydra Brute Force")
        print("7. Run John the Ripper")
        print("8. Analyze Memory with Volatility")
        print("9. Launch FTK Imager")
        print("10. Launch Autopsy")
        print("11. Analyze with Sleuth Kit")
        print("12. Run Hashcat")
        print("13. Run Medusa Brute Force")
        print("14. Run Splunk Search")
        print("15. Run OSSEC")
        print("16. Start Zeek")
        print("17. Run Lynis Security Audit")
        print("18. Run OpenVAS Scan")
        print("19. Run Nessus Scan")
        print("20. Run Qualys Scan")
        print("21. Exit")

        choice = input("Enter your choice (1-21): ")

        if choice == '1':
            target_ip = input("Enter target IP for Nmap scan: ")
            run_nmap_scan(target_ip)
        elif choice == '2':
            target_ip = input("Enter target IP for Metasploit exploit: ")
            exploit_name = input("Enter Metasploit exploit name: ")
            run_metasploit(target_ip, exploit_name)
        elif choice == '3':
            run_burp_suite()
        elif choice == '4':
            interface = input("Enter Wi-Fi interface: ")
            capture_file = input("Enter capture file path: ")
            run_aircrack(interface, capture_file)
        elif choice == '5':
            target_ip = input("Enter target IP for Nikto scan: ")
            run_nikto(target_ip)
        elif choice == '6':
            target_ip = input("Enter target IP for Hydra brute-force: ")
            username = input("Enter the username: ")
            wordlist_path = input("Enter wordlist path: ")
            run_hydra(target_ip, username, wordlist_path)
        elif choice == '7':
            password_hash_file = input("Enter the password hash file path: ")
            run_john_the_ripper(password_hash_file)
        elif choice == '8':
            dump_path = input("Enter memory dump path for Volatility analysis: ")
            analyze_memory(dump_path)
        elif choice == '9':
            run_ftk_imager()
        elif choice == '10':
            run_autopsy()
        elif choice == '11':
            analyze_with_sleuth_kit()
        elif choice == '12':
            password_hash_file = input("Enter password hash file path for Hashcat: ")
            run_hashcat(password_hash_file)
        elif choice == '13':
            target_ip = input("Enter target IP for Medusa brute-force: ")
            username = input("Enter the username: ")
            run_medusa(target_ip, username)
        elif choice == '14':
            query = input("Enter Splunk search query: ")
            run_splunk_search(query)
        elif choice == '15':
            run_ossec()
        elif choice == '16':
            start_zeek()
        elif choice == '17':
            run_lynis()
        elif choice == '18':
            target_ip = input("Enter target IP for OpenVAS scan: ")
            run_openvas_scan(target_ip)
        elif choice == '19':
            target_ip = input("Enter target IP for Nessus scan: ")
            run_nessus_scan(target_ip)
        elif choice == '20':
            target_ip = input("Enter target IP for Qualys scan: ")
            run_qualys_scan(target_ip)
        elif choice == '21':
            print("Exiting Cybersecurity Toolkit.")
            break  # Exit the program
        else:
            print("Invalid choice. Please select a number between 1 and 21.")

if __name__ == "__main__":
    main()
