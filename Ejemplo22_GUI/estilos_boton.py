import tkinter
from tkinter import ttk

root = tkinter.Tk()

style = ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'yellow')]
    )
#style.font('C.TButton','Calabri',30,'bold')

colored_btn = ttk.Button(text="Test", style="C.TButton").pack()

root.mainloop()