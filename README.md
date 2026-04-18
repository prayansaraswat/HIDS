# Mini Host-Based Intrusion Detection System (Mini HIDS)

This is a lightweight educational Host-Based Intrusion Detection System implemented in Python.
It demonstrates file integrity monitoring, log monitoring, process monitoring and optional network sniffing.

**Safe demo:** Only `tests/testfile.txt` is monitored by default so you can safely test file-change detection.

## Running (safe demo)
1. Create a virtualenv and install requirements (scapy optional):
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
   If you don't want to install scapy, set `USE_SCAPY=0` in `config.env` (default).

2. Configure (optional) `config.env` for email alerts (not required for demo).

3. Create baseline (already created for demo):
   ```bash
   python file_integrity.py --init
   ```
   (This will update baseline.json if run.)

4. Start the orchestrator (runs file, process, and log monitors):
   ```bash
   python monitor.py
   ```

5. Trigger tests:
   - File change: edit `tests/testfile.txt` and save — watch for alert in console and `hids.log`.
   - Log monitor: append lines to `tests/auth_test.log` similar to SSH failures to trigger brute-force alert:
     ```bash
     echo "Failed password for invalid user test" >> tests/auth_test.log
     ```
   - Process monitor: start an unusual process (e.g. `python -c "import time; time.sleep(300)"`) not in whitelist to trigger alert.

## Files
- `alert.py` — unified alerting (console + rotating file + optional email)
- `file_integrity.py` — create baseline and compute hashes
- `file_monitor.py` — periodic file integrity checks
- `process_monitor.py` — detects new/unknown processes vs whitelist
- `log_monitor.py` — tails and analyzes a log file (safe demo uses `tests/auth_test.log`)
- `net_monitor.py` — optional scapy-based sniffer (disabled by default)
- `monitor.py` — orchestrator to run monitors concurrently
- `baseline.json`, `whitelist.json`, `config.env` — config files
- `tests/` — contains `testfile.txt` and `auth_test.log` for safe testing

## Notes
- Do **not** run packet sniffing on networks you don't own; scapy requires root privileges.
- Use this project for educational/demo purposes only.
