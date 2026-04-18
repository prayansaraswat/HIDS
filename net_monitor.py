import os
from dotenv import load_dotenv
load_dotenv()
USE_SCAPY = os.getenv('USE_SCAPY', '0') == '1'

if not USE_SCAPY:
    print('net_monitor disabled. Set USE_SCAPY=1 in config.env to enable (requires scapy & root).')
else:
    # Lazy import scapy when needed
    try:
        from scapy.all import sniff, IP
        from alert import send_alert
        from datetime import datetime

        def pkt_cb(pkt):
            if pkt.haslayer(IP):
                ip = pkt[IP]
                send_alert(f"Packet observed: {ip.src} -> {ip.dst} at {datetime.now().isoformat()}")

        def run_sniffer():
            print('Starting scapy sniffer (this requires root).')
            sniff(prn=pkt_cb, store=False, filter='ip', timeout=0)

        if __name__ == '__main__':
            run_sniffer()
    except Exception as e:
        print('Scapy import/usage failed:', e)
