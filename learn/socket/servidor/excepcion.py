class Excepcion(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        self.causa = None
    
    def __str__(self):
        return f"Excepción lanzada por la clase: {self.__class__}"
    
class DivisionIgualCinco(Excepcion):
    def __init__(self, mensaje, causa=None):
        super().__init__(mensaje)
        self.causa = causa
        self.mensaje = mensaje
        self.causa = causa

    def __str__(self):
        return f"Excepción lanzada por la clase: {self.__class__} -{self.mensaje} - Causa: {self.causa}"


class Operaciones:
    def __init__(self, num):
        self.num = num
    
    def __ne__(self, otro):
        if self.num < 5:
            raise DivisionIgualCinco("No se puede realizar la operacion, debe ser igual a 5")
        else:
            return self.num != otro.num


if __name__=="__main__":
    try:
        # Código que puede generar una excepción
        print("Código que puede generar una excepción")
        raise Excepcion("Error en el código")
    except Excepcion as e:
        print(f"Excepción: {e.mensaje}")