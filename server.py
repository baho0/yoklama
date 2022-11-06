import socket
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 4444))
s.listen(10)
c, addr = s.accept()
print('{} connected.'.format(addr))

while True:
    m = s.recv(1024)

