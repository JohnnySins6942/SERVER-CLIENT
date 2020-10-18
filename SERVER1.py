import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = ('192.168.0.14')

s.bind((ip, 80))

s.listen(5)

while True:
    clt, adr = s.accept()
    clt.send(bytes("socket programming tutorial", "utf-8"))
    clt.close()
