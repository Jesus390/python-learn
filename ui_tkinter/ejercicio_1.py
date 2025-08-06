from tkinter import *
from tkinter import ttk
from tkinter import StringVar

import random
import time

print(time.ctime(time.time()))

def ejecutar_servidor(cantidad=10):
    print("Iniciando servidor...")
    entry_text.insert(END, "Ejecutando servidor.\n")


window = Tk()
window.title("Servidor")
window.geometry("300x300+100+100")

var_entry_text = StringVar()

frm_main = Frame(window, width=200, height=200, bg="blue")
frm_main.pack()

frm_btn = Frame(window, width=100, height=100, bg="red")
frm_btn.pack(padx=10, pady=10)

entry_text = Text(frm_main, height=10, width=50)
entry_text.pack()

btn_ejecutar_servidor = Button(frm_btn, text="Ejecutar Servidor", command=lambda: ejecutar_servidor())
btn_ejecutar_servidor.pack()

window.mainloop()