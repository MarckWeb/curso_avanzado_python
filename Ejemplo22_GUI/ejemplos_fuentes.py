import tkinter as tk
from tkinter import font


# Alternativas a tkinter
# pyqt6 ->  pip install PyQt6    https://pypi.org/project/PyQt6/  https://www.pythonguis.com/pyqt6-tutorial/  gratuita
# pyside6  ->   pip install PySide6    https://pypi.org/project/PySide6/   gratuita

ventana = tk.Tk()
# title bar
ventana.title("Ejemplo de textos")
ventana.geometry("300x300")

label1 = tk.Label(ventana, text="fuente por defecto")
label1.pack()

label2 = tk.Label(ventana, text="fuente Arial", font={"Arial"})
label2.pack()

label3 = tk.Label(ventana, text="fuente Arial con tamaño 16", font=("Arial", "16"))
label3.pack()

label4 = tk.Label(ventana, text="fuente Arial con tamaño 16", font=("Arial", 16), bg="blue", fg="white")
label4.pack()

label5 = tk.Label(ventana, text="fuente Arial con tamaño 16", font=("Comic Sans MS", "16", "bold"))
label5.pack()

label6 = tk.Label(ventana, text="fuente Arial con tamaño 16", font=("Arial", "16", "italic"))
label6.pack()

label7 = tk.Label(ventana, text="fuente Arial con tamaño 16", font=("Century Gothic", "16", "underline"))
label7.pack()

# "overstrike" no funciona en mac
label8 = tk.Label(ventana, text="fuente Arial con tamaño 16", font=("Arial", "16", "overstrike"))
label8.pack()

# Prueba para ver que no coge los colores a no ser que el boton sea del modulo tkmacosx
#from tkmacosx import Button
boton = tk.Button(ventana, text="prueba", background="yellow")
#boton.configure(activebackground="", activeforeground="")
boton.bind("<Enter>", func=lambda e: boton.config( background="yellow"))
boton.bind("<Leave>", func=lambda e: boton.config( background="black"))
boton.pack()

# para ver el tipo de fuente predeterminada
default_font =  font.nametofont("TkDefaultFont")
print(f"  fuente predeterminada   Tkinter  : {default_font.actual()}")

# ver todas las fuentes disponibles
print(font.families())

# Alternativa porque en mac no funciona overstrike
def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'  # unicode el tachado
    return result

print(strike("Probando el tachado"))

ventana.mainloop()