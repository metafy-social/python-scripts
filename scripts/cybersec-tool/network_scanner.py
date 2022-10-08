#!/usr/bin/env python3
"""A simple script used to scan a network for valid host/hosts.
   Script uses Python 3"""

import scapy.all as scapy
import argparse


def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', dest='target', help='Target IP / IP range.')
    (options) = parser.parse_args()

    return options


def scan(ip):
    """Performs ARP scan of network based on user supplied criteria."""
    arp_request = scapy.ARP(pdst=ip)                                                # sets destination IP address
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")                                # sets broadcast MAC address
    arp_request_broadcast = broadcast/arp_request                                   # creates ARP request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False) [0]  # send/receive ARP packets

    clients_list = []

    for element in answered_list:
        client_dict = {'ip': element[1].psrc, 'mac': element[1].hwsrc}
        clients_list.append(client_dict)

    return clients_list


def print_result(results_list):
    """Prints output of scan function to terminal."""
    print(f'IP\t\t\t\tMAC Address\n' + '-' * 75)                                    # output header
    for client in results_list:
        print(f'{client["ip"]}\t\t{client["mac"]}')


options = get_arguments()                                                           # captures argument from terminal
scan_result = scan(options.target)
print_result(scan_result)
