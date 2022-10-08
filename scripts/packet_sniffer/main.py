import scapy.all as scapy
from scapy.layers import http


def sniffing(interface):
    scapy.sniff(iface=interface,
                storage=False, prn=process_packet, filter='tcp')


def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(packet[http.HTTPRequest].Host)


def main():
    sniffing("Wi-Fi")


if __name__ == "__main__":
    main()
