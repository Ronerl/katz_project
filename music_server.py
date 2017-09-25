__author__ = 'master'
import socket
server = socket.socket()
port = 8820
server.bind(('0.0.0.0', port))

server.listen(5)

(client_socket, client_address) = server.accept()
print "connected!\n"

with open('music.wav', 'rb') as f:
    for l in f:
        client_socket.send(l)
client_socket.close()
server.close()