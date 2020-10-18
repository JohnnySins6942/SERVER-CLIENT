import socket
import pickle

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('connecting')
s.connect(('192.168.0.14', 80))
print('connected')
print(s.recv(1024))