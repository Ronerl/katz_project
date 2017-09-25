__author__ = 'master'
import socket
import os
server = socket.socket()
port = 8820
server.bind(('0.0.0.0', port))

server.listen(5)

(client_socket, client_address) = server.accept()
print "connected!\n"
while True:
    client_socket.send("Please choose a song!")
    filename = client_socket.recv(1024)
    if os.path.isfile(filename):
        print "sending song!"
        with open(filename, 'rb') as f:
            for l in f:
                client_socket.send(l)
        break
    else:
        client_socket.send("I don't have this song!")
client_socket.close()
server.close()