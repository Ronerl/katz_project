from imghdr import what
import socket

client_socket = socket.socket()

ip = socket.gethostbyname(socket.gethostname())
client_socket.connect((ip, 8820))

while True:
    data = raw_input("Please enter data\n")
    client_socket.send(data)
    print client_socket.recv(1024)
