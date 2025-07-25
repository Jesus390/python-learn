import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        print(">>", end=' ')
        msg = input()
        if msg == 'quit':
            break
        s.sendall(msg.encode('utf-8'))
        data = s.recv(1024)
        print('Received', data)