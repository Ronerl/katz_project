__author__ = 'master'
import socket
import select

server_socket = socket.socket()

server_socket.bind(('0.0.0.0', 8820))

server_socket.listen(-1)

open_client_sockets = []
messages_to_send = []

def send_waiting_messages(wlist):
    for message in messages_to_send:
        (client_socket, data) = message
        if client_socket in wlist:
            client_socket.send(data)
            messages_to_send.remove(message)

while True:
    rlist, wlist, xlist = select.select( [server_socket] + open_client_sockets, open_client_sockets, [])
    for current_socket in rlist:
        if current_socket is server_socket:
            (new_socket, address) = server_socket.accept()
            open_client_sockets.append(new_socket)
        else:
            data = current_socket.recv(1024)
            if data == "":
                open_client_sockets.remove(current_socket)
                print "closed"
            else:
                print data
                messages_to_send.append((current_socket, 'Hello ' + data))

    send_waiting_messages(wlist)