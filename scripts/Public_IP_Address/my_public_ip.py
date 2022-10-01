from requests import get

ip = get('https://ipv4.icanhazip.com').text

print('>>> My public IP address is: ' + ip[0:-1] + ' <<<')