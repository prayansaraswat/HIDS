#  Mini Host-Based Intrusion Detection System (HIDS)

A lightweight **educational HIDS built in Python** that monitors system activity to detect potential security threats such as file tampering, brute-force login attempts, suspicious processes, and optional network activity.

---

##  Features

*  File Integrity Monitoring (hash-based)
*  Process Monitoring (whitelist-based detection)
*  Brute-force Detection (log analysis)
*  Network Monitoring (Scapy-based, optional)
*  Real-time Alerts (console + log file)

---

##  Safe Demo Environment

This project includes a **safe testing setup**:

* Only `tests/testfile.txt` is monitored for file changes
* Log monitoring uses `tests/auth_test.log`
* No real system files are modified

---

##  Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

 Optional: Disable network monitoring if Scapy not installed
Set in `config.env`:

```
USE_SCAPY=0
```

---

##  Running the Project

### 1. Create baseline

```bash
python file_integrity.py --init
```

### 2. Start all monitors

```bash
python monitor.py
```

---

##  Testing Features

###  File Integrity

```bash
echo "test" >> tests/testfile.txt
```

---

###  Brute-force Detection

```bash
echo "Failed password for invalid user test" >> tests/auth_test.log
```

---

###  Process Monitoring

```bash
python -c "import time; time.sleep(300)"
```

---

###  Network Monitoring (optional)

```bash
sudo $(which python) monitor.py
```

---

##  Project Structure

```
mini_hids_code/
│── monitor.py            # Main orchestrator
│── file_monitor.py       # File monitoring
│── process_monitor.py    # Process monitoring
│── log_monitor.py        # Log analysis
│── net_monitor.py        # Network sniffing
│── alert.py              # Alert system
│── baseline.json         # File hashes
│── whitelist.json        # Allowed processes
│── config.env            # Configuration
│── tests/                # Safe demo files
```

---

##  Notes

* Network monitoring requires **root privileges**
* Do not use packet sniffing on unauthorized networks
* Designed for educational use and security research; can be extended for real-world monitoring scenarios.
---

##  Impact

Provides **real-time detection of system-level security threats** and demonstrates how HIDS works in practice.

---

##  Tech Stack

* Python
* psutil
* hashlib
* scapy (optional)
* python-dotenv

---

