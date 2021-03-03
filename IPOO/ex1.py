import tkinter as tk
from tkinter import messagebox
import ast

window = tk.Tk()

class circulo():
    def __init__(self):
        self.PI = 3.1415
    def area(self, raio):
        
        raio = ast.literal_eval(raio)
        return round(((raio * raio) * self.PI), 2)

tk.Label(window, text = "Digite o raio do circulo: ").grid(row = 0)
raio = tk.Entry()
raio.grid(row = 0, column = 1)

Circulo = circulo()
def calcula():
    calculo = Circulo.area(raio.get())
    messagebox.showinfo("Calculo", "A área do círculo é " + str(calculo))

tk.Button(window, text = "Calcular", command = calcula).grid(row = 1)

window.mainloop()