import tkinter as tk
from tkinter import messagebox

def boton_info():
    respuesta = messagebox.showinfo("Titulo","Mensaje de informacion")
    print(respuesta) # ok

def boton_askyesno():
    respuesta = messagebox.askyesno("Titulo","Estas de acuerdo?", icon="info")
    print(respuesta) # True(yes) False(no)

def boton_askokcancel():
    respuesta = messagebox.askokcancel("Titulo","Estas seguro que lo quieres eliminar?")
    print(respuesta) # True(ok) False(Cancelar)

def boton_askretraycancel():
    respuesta = messagebox.askretrycancel("Titulo","Ha habido un problema...")
    print(respuesta) # True(Reintentar) False(Cancelar)

def boton_askquestion():
    respuesta = messagebox.askquestion("Titulo","Cerramos ventana?", icon="question")
    print(respuesta) # yes no

def boton_showerror():
    respuesta = messagebox.showerror("Titulo","Error grave")
    print(respuesta) # ok

def boton_showwarning():
    respuesta = messagebox.showwarning("Titulo","Mensaje de aviso")
    print(respuesta) # ok

ventana = tk.Tk()
ventana.title("Ejemplo de los metodos messagebox")
ventana.geometry("300x300")
boton_info = tk.Button(ventana, text='showinfo', command=boton_info)
boton_info.pack()
boton_si_no = tk.Button(ventana, text='askyesno', command=boton_askyesno)
boton_si_no.pack()
boton_cancel = tk.Button(ventana, text='askokcancel', command=boton_askokcancel)
boton_cancel.pack()
boton_retry = tk.Button(ventana, text='askretrycancel', command=boton_askretraycancel)
boton_retry.pack()
boton_question = tk.Button(ventana, text='askquestion', command=boton_askquestion)
boton_question.pack()
boton_error = tk.Button(ventana, text='showerror', command=boton_showerror)
boton_error.pack()
boton_warning = tk.Button(ventana, text='showwarning', command=boton_showwarning)
boton_warning.pack()

ventana.mainloop()