# Simple Port Scanner
This is a simple port scanner written in Python. You can run a scan on any one particular host or over a given range of IP addresses.

Download the script on your local machine and use as follows.

## Usage
- Single host - scans a single IP address

    `./scanner.py <IP address> <start port> <end port>`
    _Example:`./scanner.py 192.168.0.17 1 65535`_

- Network scan - scans a range of IP addresses
    
    `./scanner.py <network> <start port> <end port> -n`
    _Example:`./scanner.py 192.168.0 1 65535 -n`_
