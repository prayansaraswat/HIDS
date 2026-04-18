import hashlib, json, os, argparse
from pathlib import Path

MONITOR_FILES = [
    # For safe demo we monitor only the test file in tests/
    str(Path(__file__).resolve().parent / 'tests' / 'testfile.txt')
]

def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def create_baseline(files, out='baseline.json'):
    baseline = {}
    for p in files:
        if os.path.exists(p):
            try:
                baseline[p] = sha256(p)
            except Exception as e:
                print('Skipping', p, ':', e)
    with open(out, 'w') as f:
        json.dump(baseline, f, indent=2)
    print('Baseline saved to', out)
    return baseline

def load_baseline(path='baseline.json'):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create or show baseline hashes.')
    parser.add_argument('--init', action='store_true', help='Create baseline file using default MONITOR_FILES')
    parser.add_argument('--show', action='store_true', help='Show current baseline')
    args = parser.parse_args()

    if args.init:
        create_baseline(MONITOR_FILES)
    elif args.show:
        print(load_baseline())
    else:
        print('Run with --init to create baseline or --show to view it.')
