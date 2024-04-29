import tkinter as tk
from tkinter import ttk

# crear una nueva ventana
ventana = tk.Tk()
ventana.title('Ejemplo de widgets')
ventana.geometry('400x600+500+200')  # anchoxalto+desp_x+desp_y

# Añadir los widgets a la ventana
boton = tk.Button(ventana, text='Pulsame')
boton.place(x=10,y=20)



# crear un frame
frame_1 = tk.LabelFrame(ventana, width=400, height=150, text="Datos Personales")
frame_1.place(x=10, y= 50)

etiqueta = tk.Label(frame_1, text='Introduce tu nombre:', bg='blue', fg='#DC9DF3')
etiqueta.place(x=10, y=50)
caja_texto = tk.Entry(frame_1,width=20)
caja_texto.place(x=150, y=50)

password = tk.Entry(frame_1, show='*')
password.place(x=10, y=80)

mystr = tk.StringVar()
mystr.set('This is the default text')
caja_texto_deshabilitada = tk.Entry(frame_1,width=20, state='readonly', textvariable=mystr)
caja_texto_deshabilitada.place(x=200, y=80)

acepto = tk.Checkbutton(ventana,text='Acepto condiciones')
acepto.place(x=200, y= 200)

sexo_var = tk.StringVar()
sexo_h = tk.Radiobutton(ventana, text="Hombre", variable=sexo_var, value="H")
sexo_m = tk.Radiobutton(ventana, text="Mujer", variable=sexo_var, value="M")
sexo_h.place(x=10, y= 250)
sexo_m.place(x=100, y= 250)

colores = ['Azul','Rosa','Amarillo','Verde']
color = tk.Listbox(ventana, selectmode='multiple', activestyle="dotbox")
for item in colores:
    color.insert(tk.END, item)
color.place(x=10, y=300)

colores_2= ['--Selecciona--'] + colores
combo = tk.ttk.Combobox(ventana, values=colores_2, state="readonly")
combo.current(0)
combo.place(x=10, y=480)

# Crear un combobox (selector)
opciones = ['--Selecciona--',"Opción 1", "Opción 2", "Opción 3"]
combobox = tk.OptionMenu(ventana, tk.StringVar(ventana), *opciones)
combobox.place(x=10, y = 550)


# mostrar la ventana
ventana.mainloop()