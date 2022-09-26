# a simple script to block websites
from datetime import datetime
import sys

if sys.platform == 'win32':
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
else:
    hosts_path = '/private/etc/hosts'

redirect = "127.0.0.1"


class Blocker:
    def __init__(self, time, block):
        self.time = time
        self.block = block

    def block_websites(self):
        if datetime.now() < self.time:
            print("Block sites")
            with open(hosts_path, 'r+') as hostfile:
                hosts_content = hostfile.read()
                for site in self.block:
                    if site not in hosts_content:
                        hostfile.write(redirect + "  " + site + "\n")
        else:
            print('Unblock sites')
            with open(hosts_path, 'r+') as hostfile:
                lines = hostfile.readlines()
                hostfile.seek(0)
                for line in lines:
                    if not any(site in line for site in self.block):
                        hostfile.write(line)
                hostfile.truncate()


# sudo python main.py
if __name__ == '__main__':
    end_time = datetime(2021, 10, 1, 20)  # y, m, d, h, min
    sites_to_block = ['www.facebook.com', 'facebook.com']
    block = Blocker(end_time, sites_to_block)
    block.block_websites()
