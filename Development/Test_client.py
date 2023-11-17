import socket

host = "10.32.48.246"
port = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    i = int(input("1,2,3"))
    if i ==1:
        s.sendall(b'ABS_up')
    if i == 2:
        s.sendall(b'ABS_down')
    if i == 3:
        s.sendall(b'TC1_up')
    print(s.recv(1024))
