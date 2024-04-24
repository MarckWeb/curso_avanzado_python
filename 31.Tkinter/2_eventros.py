import tkinter as tk
from tkinter import messagebox


def boton_info():
    resp = messagebox.showinfo('Detalle', 'Mensaje de informacion')
    print(resp)  # OK


def boton_askyesno():
    resp = messagebox.askyesno('Titulo', 'Estas de acuerdo')
    print(resp)  # TRUE OR FALSE


def boton_askokcancel():
    resp = messagebox.askokcancel(
        'Titulo', message='estas seguro de que quieres eliminar')
    print(resp)


def boton_askretrycancel():
    resp = messagebox.askretrycancel('Titulo', 'Ha habido un problema')
    print(resp)


def boton_askquestion():
    resp = messagebox.askquestion('Titulo', 'Cerramos la ventana?')
    print(resp)


def boton_showerror():
    resp = messagebox.showerror('Titulo', 'Error grave')
    print(resp)


def boton_showwarning():
    resp = messagebox.showwarning('Titulo', 'Mensaje de aviso')
    print(resp)


# crear una nueva ventana
ventana = tk.Tk()
ventana.title('Ejemplo de widgets')
ventana.geometry('300x300')

boton = tk.Button(ventana, text='showinfo', command=boton_info)
boton.pack()

boton_si_no = tk.Button(ventana, text='askyesno', command=boton_askyesno)
boton_si_no.pack()

boton_cancel = tk.Button(ventana, text='askokcancel',
                         command=boton_askokcancel)
boton_cancel.pack()

boton_retry = tk.Button(ventana, text='askretrycancel',
                        command=boton_askretrycancel)
boton_retry.pack()

boton_question = tk.Button(ventana, text='askquestion',
                           command=boton_askquestion)
boton_question.pack()

boton_errores = tk.Button(ventana, text='showerror', command=boton_showerror)
boton_errores.pack()

boton_warning = tk.Button(ventana, text='showwarning',
                          command=boton_showwarning)
boton_warning.pack()


# final
ventana.mainloop()
