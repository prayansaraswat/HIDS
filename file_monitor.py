import time, json, os
from file_integrity import sha256, load_baseline
from alert import send_alert

BASELINE_FILE = 'baseline.json'
CHECK_INTERVAL = 10  # seconds

def monitor_files():
    baseline = load_baseline(BASELINE_FILE)
    if not baseline:
        print('No baseline found. Run file_integrity.py --init first.')
        return
    print('Starting file monitor. Monitoring {} files.'.format(len(baseline)))
    while True:
        updated = False
        for path, old_hash in list(baseline.items()):
            if not os.path.exists(path):
                send_alert(f"Monitored file missing: {path}")
                continue
            try:
                new_hash = sha256(path)
            except Exception as e:
                continue
            if new_hash != old_hash:
                send_alert(f"File integrity change detected: {path}")
                # Update the baseline so repeated alerts don't spam; manual review recommended
                baseline[path] = new_hash
                updated = True
        if updated:
            with open(BASELINE_FILE, 'w') as f:
                json.dump(baseline, f, indent=2)
        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    monitor_files()
