#!/usr/bin/python3
from logging import exception
import socket
import sys

def scanHost(ip, startPort, endPort):
    """ Starts a TCP scan on any given IP address """

    print('[*] Starting TCP port scan on host %s' % ip)

    # Begin TCP scan on host
    tcp_scan(ip, startPort, endPort)

    print('[+] TCP scan on host %s complete' % ip)


def scanRange(network, startPort, endPort):
    """ Starts a TCP scan on a given IP address range """

    print('[*] Starting TCP port scan on network %s.0' % network)

    # Iterate over a range of host IP addresses and scan each target
    for host in range(1, 255):
        ip = network + '.' + str(host)
        tcp_scan(ip, startPort, endPort)

    print('[+] TCP scan on network %s.0 complete' % network)


def tcp_scan(ip, startPort, endPort):
    """ Creates a TCP socket and attempts to connect via supplied ports """

    for port in range(startPort, endPort + 1):
        try:
            # Create a new socket
            tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Print if the port is open
            if not tcp.connect_ex((ip, port)):
                print('[+] %s:%d/TCP Open' % (ip, port))
                tcp.close()
                
        except Exception:
            pass


if __name__ == '__main__':
    # Timeout in seconds
    socket.setdefaulttimeout(0.01)

    try:
        network   = sys.argv[1]
        startPort = int(sys.argv[2])
        endPort   = int(sys.argv[3])

        if len(sys.argv) == 4:
            scanHost(network, startPort, endPort)

        elif len(sys.argv) == 5 and sys.argv[4] == "-n":
            scanRange(network, startPort, endPort)
        
        else:
            raise exception
    
    except:
        print('Error: unrecognized or incomplete command line')
        print('usage: ./scanner.py <IP address> <start port> <end port>')
        print('example: ./scanner.py 192.168.0.17 1 65535\n')
        print('usage: ./scanner.py <network> <start port> <end port> -n')
        print('Example: ./scanner.py 192.168.0 1 65535 -n')