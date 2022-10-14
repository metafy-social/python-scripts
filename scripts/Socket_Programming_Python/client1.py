
import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 1024
host = socket.gethostbyname(socket.gethostname())  # get the hostname
client_socket.connect((host, port))
message = client_socket.recv(2048)
print(message.decode("utf-8"))
