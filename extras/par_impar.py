import os

def write_par_impar(n:int=10000) -> None:
    '''
    Crea un archivo 'par_impar.py' con código Python para imprimir
    si un número es par o impar utilizando solamente condicionales.

    Parámetros
    -----------
    n : int
    Número de iteraciones para el bucle.
    '''
    with open('par_impar_.py', 'w', encoding='utf-8') as archivo:
        archivo.write('def par_impar(n: int) -> None:\n')
        archivo.write('    """\n')
        archivo.write('    Imprime si el número es par o impar.\n\n')
        archivo.write('    Parámetros\n')
        archivo.write('    ----------\n')
        archivo.write('    n : int\n')
        archivo.write('    """\n')
        archivo.write('    num = int(input("Ingrese el número y le diré si es par o impar: "))\n')
        for i in range(n+1):
            if i == 0:
                archivo.write(f'    if num == {i}:\n')
                archivo.write(f'        print(f"El número es par")\n')
            elif i == n:
                if i % 2 == 0:
                    archivo.write(f'    else:\n')
                    archivo.write(f'        print(f"El número es par")\n')
                else:
                    archivo.write(f'    else:\n')
                    archivo.write(f'        print(f"El número es impar")\n')
            else:
                if i % 2 == 0:
                    archivo.write(f'    elif num == {i}:\n')
                    archivo.write(f'        print(f"El número es par")\n')
                else:
                    archivo.write(f'    elif num == {i}:\n')
                    archivo.write(f'        print(f"El número es impar")\n')
        archivo.write("\n\nif __name__=='__main__':\n")
        archivo.write("    par_impar(10000)")
        print(f'Archivo "par_impar.py" creado con éxito')
        
if __name__=="__main__":
    write_par_impar(100)