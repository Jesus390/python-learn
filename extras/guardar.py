import os

class Guardar():
    carpeta_contenedora_de_archivos = 'datos'

    def categorias_como_csv(self, filename, datos):
        if self._carpeta_existe(self.carpeta_contenedora_de_archivos):
            ruta = os.path.join(self.carpeta_contenedora_de_archivos, filename)
        else:
            os.makedirs(self.carpeta_contenedora_de_archivos)
            ruta = os.path.join(self.carpeta_contenedora_de_archivos, filename)
        if self._archivo_existe(ruta):
            print(f"Open: {ruta}.csv...")
        else:
            print(f"Creating: {ruta}.csv...")
            print(f"Succesfully: {ruta}.csv creado con éxito.")
            print(f"Open: {ruta}.csv...")

        with open(self.carpeta_contenedora_de_archivos + "/" + filename + '.csv', 'w') as archivo:
            print("Writing: categoria,link")
            archivo.write("categoria,link\n")
            for key, value in datos.items():
                print(f"Writing: {key},{value}")
                archivo.write(f"{key},{value}{'\n' if key != list(datos.keys())[-1] else ''}")
            print(f"Message: Datos cargados al archivo {ruta}.csv con éxito.")
            print(f"Closed: Archivo {ruta}.csv")

    def libros_como_csv(self, filename, datos):
        if self._carpeta_existe(self.carpeta_contenedora_de_archivos):
            ruta = os.path.join(self.carpeta_contenedora_de_archivos, filename)
        else:
            os.makedirs(self.carpeta_contenedora_de_archivos)
            ruta = os.path.join(self.carpeta_contenedora_de_archivos, filename)
        if self._archivo_existe(ruta):
            print(f"Open: {ruta}.csv...")
        else:
            print(f"Creating: {ruta}.csv...")
            print(f"Succesfully: {ruta}.csv creado con éxito.")
            print(f"Open: {ruta}.csv...")

        with open(ruta + '.csv', 'w') as archivo:
            print("Writing: categoria,link")
            archivo.write("categoria,link\n")
            for key, value in datos.items():
                # print("Guardando: ", key, value)
                for item in value:
                    print(f"Writing: {key},{value}")
                    archivo.write(f"{key},{item['link']}{'\n' if key != list(datos.keys())[-1] else ''}")
                    
            print(f"Message: Datos cargados al archivo {ruta}.csv con éxito.")
            print(f"Closed: Archivo {ruta}.csv")

    def _archivo_existe(self, filename):
        return os.path.exists(filename + ".csv")
    
    def _carpeta_existe(self, carpeta):
        return os.path.exists(carpeta)

