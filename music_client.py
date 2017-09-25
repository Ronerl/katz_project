__author__ = 'master'
import socket, winsound
server = socket.socket()
port = 8820
ip = socket.gethostbyname(socket.gethostname())
my_socket = socket.socket()
my_socket.connect((ip, port))

with open('my_music.wav','wb') as f:
  while True:
    l = my_socket.recv(1024)
    if not l: break
    f.write(l)
my_socket.close()

winsound.PlaySound("my_music.wav", winsound.SND_FILENAME)
