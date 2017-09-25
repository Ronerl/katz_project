__author__ = 'master'
import socket
import os
server = socket.socket()
port = 8820
server.bind(('0.0.0.0', port))

server.listen(5)

(client_socket, client_address) = server.accept()
print "connected!\n"
def send_wav(filename, client):
    with open(filename, 'rb') as f:
            for l in f:
                client.send(l)

while True:
    client_socket.send("Please choose a song!\n")
    filename = client_socket.recv(1024)
    if os.path.isfile(filename):
        print "sending song!"
        send_wav(filename,client_socket)
        break
    elif os.path.isdir(filename):
        for filet in os.listdir():
            send_wav(filet, client_socket)
        break
    else:
        client_socket.send("I don't have this song!")
client_socket.close()
server.close()