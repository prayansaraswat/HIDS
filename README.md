# HIDS
A lightweight Python-based Host-Based Intrusion Detection System (HIDS) that monitors files, processes, system logs, and network activity to detect and alert on potential security threats in real time.

# Features
 File Integrity Monitoring
Detects unauthorized file modifications using hashing
 Process Monitoring
Identifies newly spawned or suspicious processes
Brute-Force Detection
Detects repeated failed SSH login attempts
 Network Monitoring
Captures and analyzes network packets using Scapy
 Real-Time Alerts
Displays alerts instantly in the terminal

Tech Stack
Language: Python
OS: Linux (Arch recommended)
Libraries:
psutil – process monitoring
hashlib – file integrity
scapy – network sniffing
python-dotenv – configuration handling

mini_hids_code/
│── monitor.py            # Main entry point
│── file_monitor.py       # File integrity module
│── process_monitor.py    # Process monitoring module
│── log_monitor.py        # Brute-force detection
│── net_monitor.py        # Network monitoring
│── alert.py              # Alert system
│── config.env            # Configuration file
│── requirements.txt      # Dependencies
│── tests/                # Test files/logs

# Clone the repository
git clone https://github.com/prayansaraswat/HIDS.git

# Navigate to project
cd mini_hids_code

# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Full HIDS
sudo $(which python) monitor.py

# Brute-force detection
ssh wronguser@localhost

# File monitoring
echo "test" >> tests/testfile.txt

# Process monitoring
sleep 60 &

# Network monitoring
ping 8.8.8.8

