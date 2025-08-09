from scapy.all import sniff, IP
from collections import defaultdict
import time
from logger import log_alert

PACKET_THRESHOLD = 100  # packets
TIME_WINDOW = 10  # seconds

ip_traffic = defaultdict(list)

def analyze_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        now = time.time()
        ip_traffic[src_ip].append(now)

        # Keep only timestamps within the time window
        ip_traffic[src_ip] = [t for t in ip_traffic[src_ip] if now - t <= TIME_WINDOW]

        # Check for DoS pattern
        if len(ip_traffic[src_ip]) > PACKET_THRESHOLD:
            alert_msg = f"[!] DoS Alert: {src_ip} sent {len(ip_traffic[src_ip])} packets in {TIME_WINDOW}s"
            print(alert_msg)
            log_alert(alert_msg)

def start_monitoring(interface):
    print(f"[+] Monitoring on {interface}...")
    sniff(iface=interface, prn=analyze_packet, store=False)
