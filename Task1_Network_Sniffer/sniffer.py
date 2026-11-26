from scapy.all import sniff, wrpcap, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

captured_packets = []

def get_protocol(packet):
    if packet.haslayer(TCP):
        return "TCP"
    elif packet.haslayer(UDP):
        return "UDP"
    elif packet.haslayer(ICMP):
        return "ICMP"
    return "Other"

def process_packet(packet):
    if not packet.haslayer(IP):
        return

    captured_packets.append(packet)
    ip = packet[IP]
    proto = get_protocol(packet)
    time_now = datetime.now().strftime("%H:%M:%S")

    print("=" * 60)
    print(f"[{time_now}] Packet #{len(captured_packets)}")
    print(f"Source IP      : {ip.src}")
    print(f"Destination IP : {ip.dst}")
    print(f"Protocol       : {proto}")
    print(f"Packet Size    : {len(packet)} bytes")

    if packet.haslayer(TCP):
        print(f"Src Port: {packet[TCP].sport} | Dst Port: {packet[TCP].dport}")
        print(f"TCP Flags      : {packet[TCP].flags}")
    elif packet.haslayer(UDP):
        print(f"Src Port: {packet[UDP].sport} | Dst Port: {packet[UDP].dport}")

    if packet.haslayer(Raw):
        payload = bytes(packet[Raw].load)[:50]
        print(f"Payload (50 bytes): {payload}")

def main():
    print("Network Sniffer started... Stop karne ke liye Ctrl+C dabayein.\n")
    try:
        sniff(prn=process_packet, store=False)
    except KeyboardInterrupt:
        pass
    finally:
        if captured_packets:
            wrpcap("capture.pcap", captured_packets)
            print(f"\n{len(captured_packets)} packets 'capture.pcap' mein save ho gaye.")

if __name__ == "__main__":
    main()