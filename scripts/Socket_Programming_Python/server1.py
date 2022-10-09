import socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 1024
host = socket.gethostbyname(socket.gethostname())  # get the hostname
server_socket.bind((host, port))
server_socket.listen(2)
while True:
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    conn.send(bytes("Socket programming in python","utf-8"))
