import threading, time
from file_monitor import monitor_files
from process_monitor import monitor_processes
from log_monitor import monitor_log
import os

threads = [
    threading.Thread(target=monitor_files, daemon=True),
    threading.Thread(target=monitor_processes, daemon=True),
    threading.Thread(target=monitor_log, daemon=True),
]

def main():
    for t in threads:
        t.start()
    print('All monitors started. Press Ctrl+C to stop.')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('Stopping monitors...')

if __name__ == '__main__':
    main()
