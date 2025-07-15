import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"Bind server: {HOST}:{PORT}")
    s.bind((HOST, PORT))
    print(f"Server listening...")
    s.listen()
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Nueva conección: {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)