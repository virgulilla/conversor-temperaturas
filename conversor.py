from tkinter import *
from functions import to_celsius, to_fahrenheit
from typing import Union

def a_float(cadena: str) -> Union[float, str]:
    try:
        return float(cadena)
    except ValueError:
        return ""

def event(p: str):
    temperatura = a_float(valor.get())
    if temperatura == "":
        res = "Temperatura no numerica"
    elif p == 'C':
        res = f"{to_celsius(temperatura)}°C"
    elif p == 'F':
        res = f"{to_fahrenheit(temperatura)}°F"
    else:
        res = "Opcion incorrecta"        

    salida.config(text=res)

root = Tk()
root.title("Conversor de temperaturas")
print(root.geometry("300x250"))

valor = StringVar()

entrada = Entry(root, textvariable=valor)
entrada.pack(side=TOP, expand=True, fill=BOTH, padx=8, pady=8)
salida = Label(root, text="Soy la salida", bd=2, relief="groove")
salida.pack(side=TOP, expand=True, fill=BOTH, padx=8, pady=8)
btn_a_c = Button(root, text="Convertir a Celsius", command=lambda: event('C'))
btn_a_c.pack(side=TOP, expand=True, fill=BOTH, padx=8, pady=8)
btn_a_f = Button(root, text="Convertir a Fahrenheit", command=lambda: event('F'))
btn_a_f.pack(side=TOP, expand=True, fill=BOTH, padx=8, pady=8)



root.mainloop()