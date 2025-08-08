import socket

class Cliente:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def conectar(self):
        self.client.connect((self.host, self.port))

    def leer_dato(self):
        return self.client.recv(1024).decode('utf-8')
    
    def enviar_dato(self, mensaje):
        self.client.send(mensaje.encode('utf-8'))

    def cerrar(self):
        self.client.close()

if __name__=="__main__":
    cliente = Cliente('127.0.0.1', 12345)
    cliente.conectar()
    cliente.enviar_dato('Hola, soy el cliente')
    print(cliente.leer_dato())
    cliente.cerrar()