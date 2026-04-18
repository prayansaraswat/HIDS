import time, re, os
from collections import deque
from alert import send_alert

# Default to safe test log in tests/
DEFAULT_LOG = os.path.join(os.path.dirname(__file__), 'tests', 'auth_test.log')
LOGFILE = os.getenv('HIDS_LOGFILE', DEFAULT_LOG)
PATTERN = re.compile(r'Failed password', re.IGNORECASE)
WINDOW = 60  # seconds window
THRESHOLD = 5  # failures to trigger alert

def tail(f):
    f.seek(0,2)  # go to end
    while True:
        line = f.readline()
        if not line:
            time.sleep(0.5)
            continue
        yield line

def monitor_log():
    attempts = deque()
    try:
        with open(LOGFILE) as f:
            print(f'Log monitor started on {LOGFILE}')
            for line in tail(f):
                if PATTERN.search(line):
                    ts = time.time()
                    attempts.append(ts)
                    while attempts and attempts[0] < ts - WINDOW:
                        attempts.popleft()
                    if len(attempts) >= THRESHOLD:
                        send_alert(f"Brute-force like activity: {len(attempts)} failures in last {WINDOW}s")
                        attempts.clear()
    except FileNotFoundError:
        print('Log file not found:', LOGFILE)

if __name__ == '__main__':
    monitor_log()
