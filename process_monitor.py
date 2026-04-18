import psutil, time, json, os
from alert import send_alert

WHITELIST_FILE = 'whitelist.json'
CHECK_INTERVAL = 5  # seconds

def load_whitelist():
    if os.path.exists(WHITELIST_FILE):
        with open(WHITELIST_FILE) as f:
            return set(json.load(f))
    # default minimal whitelist
    return set(['init', 'systemd', 'python3', 'python', 'bash'])

def monitor_processes():
    whitelist = load_whitelist()
    print('Process monitor started. Whitelist contains', len(whitelist), 'entries.')
    seen = set()
    while True:
        for p in psutil.process_iter(['pid', 'name']):
            try:
                name = (p.info.get('name') or '<unknown>').lower()
            except Exception:
                continue
            key = (p.pid, name)
            if key not in seen:
                if name not in whitelist:
                    send_alert(f"New process detected: PID={p.pid} NAME={name}")
                seen.add(key)
        time.sleep(CHECK_INTERVAL)

if __name__ == '__main__':
    monitor_processes()
