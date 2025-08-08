import socket

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
    
    def acceptar(self):
        client_socket, address = self.server_socket.accept()
        return client_socket, address
    
    def leer(self, cliente_sock):
        data = cliente_sock.recv(1024)

    def enviar(self, cliente_sock, mensaje):
        return cliente_sock.send(mensaje.encode('utf-8'))
    
    def cerrar(self):
        self.server_socket.close()

if __name__=="__main__":
    HOST, PORT = '127.0.0.1', 12345
    server = Server(HOST, PORT)
    print(f"Iniciando servidor: {HOST}:{PORT}")
    server.start()
    while True:
        cliente_sock, address = server.acceptar()
        print(f"Conectado a {address}")
        data = server.leer(cliente_sock)
        print(f"Mensaje recibido: {data}")
        server.enviar(cliente_sock, "Hola, cliente")
