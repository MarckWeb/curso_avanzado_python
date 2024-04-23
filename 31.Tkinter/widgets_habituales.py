import tkinter as tk
from tkinter import ttk

# crear una nueva ventana
ventana = tk.Tk()
ventana.title('Ejemplo de widgets')

ventana.geometry('500x500+1000+200')  # (anchoXalto+despX+despY)

# LabelFrame con título
label_frame = tk.LabelFrame(
    ventana, width=400, height=300, text='Datos personales')
label_frame.place(x=50, y=50)


# Añadir los widgets a la ventana
boton = tk.Button(ventana, text='Pulsame')  # declaramos
boton.place(x=50, y=20)  # donde lo queremos colocar

# titulo de label
etiqueta = tk.Label(ventana, text='Nombre:', bg='#000',
                    fg='white', borderwidth=2, relief='groove')
etiqueta.place(x=60, y=80)

# input para ingresar valor
caja_text = tk.Entry(ventana, width=50)
caja_text.place(x=130, y=80)

# titulo de label
etiqueta = tk.Label(ventana, text='Contraseña:', bg='#000',
                    fg='white', borderwidth=2, relief='groove')
etiqueta.place(x=60, y=120)

# input para ingresar contraseña
password = tk.Entry(ventana, show='*')
password.place(x=130, y=120)


etiqueta = tk.Label(ventana, text='Email:', bg='#000',
                    fg='white', borderwidth=2, relief='groove')
etiqueta.place(x=60, y=160)
# StringVar para la caja de texto deshabilitada
valor_predeterminado = tk.StringVar(value='Example@hotmail.es')

# caja de texto deshabilitada
caja_text_deshabilitada = tk.Entry(
    ventana,
    width=20,
    textvariable=valor_predeterminado,
    state='disabled'
)
caja_text_deshabilitada.place(x=130, y=160)


# inpust radio
sexo_var = tk.Label(ventana, text='Sexo:', bg='#000',
                    fg='white', borderwidth=2, relief='groove')
sexo_var.place(x=60, y=200)

sexo_m = tk.Radiobutton(ventana, text='Masculino',
                        variable=sexo_var, value='M')
sexo_f = tk.Radiobutton(ventana, text='Femenino', variable=sexo_var, value='F')
sexo_m.place(x=130, y=200)
sexo_f.place(x=230, y=200)

# input select
lenguajes = ['JavaScript', 'TypeScript', 'Pyhton', 'BashScript']
lenguaje = tk.Listbox(ventana, selectmode='multiple',
                      activestyle='dotbox')

for item in lenguajes:
    lenguaje.insert(tk.END, item)
lenguaje.place(x=130, y=240)

# input select2
lenguajes2 = ['--Selecciona--'] + lenguajes
combo = ttk.Combobox(ventana, values=lenguajes2, state='readonly')
combo.current(0)
combo.place(x=200, y=240)


# Checkbox
privacidad = tk.Checkbutton(ventana, text='Acepto las condiciones')
privacidad.place(x=150, y=400)

# Mostrar la ventana
ventana.mainloop()
