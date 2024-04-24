import tkinter as tk

ventana = tk.Tk()
ventana.title('Ejemplos de diferentes cursores')
ventana.geometry('300x400+800+100')

label1 = tk.Label(ventana, text='arrow', cursor='arrow')
label1.pack()

label2 = tk.Label(ventana, text='clock', cursor='clock')
label2.pack()

label3 = tk.Label(ventana, text='circle', cursor='circle')
label3.pack()

label3 = tk.Label(ventana, text='arrow', cursor='cross')
label3.pack()
'''
cursores que puedes usar en Tkinter:

tcursor: Este es el cursor predeterminado de la aplicación.
arrow: El cursor de flecha estándar.
circle: Un cursor circular.
clock: Un cursor en forma de reloj.
cross: Un cursor en forma de cruz.
dotbox: Un cursor en forma de caja con un punto en el centro.
exchange: Un cursor de intercambio.
fleur: Un cursor en forma de flor.
heart: Un cursor en forma de corazón.
man: Un cursor en forma de hombre.
mouse: Un cursor en forma de ratón.
pirate: Un cursor pirata.
plus: Un cursor en forma de signo más.
shuttle: Un cursor en forma de transbordador.
sizing: Un cursor de cambio de tamaño.
spider: Un cursor en forma de araña.
spraycan: Un cursor en forma de aerosol.
star: Un cursor en forma de estrella.
target: Un cursor en forma de objetivo.
trek: Un cursor en forma de viaje.
watch: Un cursor en forma de reloj.
'''
ventana.mainloop()
