__author__ = 'master'
import socket, winsound
server = socket.socket()
port = 8820
# ip = socket.gethostbyname(socket.gethostname())
ip = '172.17.2.61'
my_socket = socket.socket()
my_socket.connect((ip, port))
print my_socket.recv(1024)
filename = raw_input("Please enter a filename!")
my_socket.send(filename)
with open('my_music.wav','wb') as f:
  while True:
    l = my_socket.recv(1024)
    if not l: break
    f.write(l)
my_socket.close()

winsound.PlaySound("my_music.wav", winsound.SND_FILENAME)
