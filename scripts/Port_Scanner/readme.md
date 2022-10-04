# Simple Port Scanner

This is a simple port scanner written in Python. You can run a scan on any one particular host or over a given range of IP addresses.

Download the script on your local machine and use as follows.
<p align="center">
  <img
    src="https://user-images.githubusercontent.com/28898632/193796899-8c27a4d9-fecc-4378-9324-bded40abc641.png"
  >
</p>

## Usage
- Single host - scans a single IP address

    ```python
    ./scanner.py <IP address> <start port> <end port>
    ```

    _Example:`./scanner.py 192.168.0.17 1 65535`_

- Network scan - scans a range of IP addresses
    
    ```python
    ./scanner.py <network> <start port> <end port> -n
    ```

    _Example:`./scanner.py 192.168.0 1 65535 -n`_
