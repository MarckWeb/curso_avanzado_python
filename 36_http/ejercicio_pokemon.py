import tkinter as tk
from PIL import Image, ImageTk
import requests
import io


def buscar_pokemon():
    nombre_pokemon = caja_text.get()
    try:
        resp = requests.get(
            f'https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}'
        )
        dato = resp.json()
        if resp.status_code == requests.codes.ok:
            print(dato['name'])
            print(dato['sprites']['front_default'])

            nombre.config(text="Nombre: " + dato['name'])

            # Cargar la imagen desde la URL
            response = requests.get(dato['sprites']['front_default'])
            img_data = response.content
            img = Image.open(io.BytesIO(img_data))
            # Redimensionar sin especificar resample
            img = img.resize((200, 200))
            photo = ImageTk.PhotoImage(img)
            imagen.config(image=photo)
            # Evitar que la imagen sea recolectada por el recolector de basura de Python
            imagen.image = photo

    except requests.RequestException:
        etiqueta.config(text='Ha ocurrido un error al buscar el Pokémon')


# Crear una nueva ventana
ventana = tk.Tk()
ventana.title('Buscar Pokemons')
ventana.geometry('500x500+1000+200')

# Título de label
etiqueta = tk.Label(ventana, text='Nombre Pokemon:', bg='#000',
                    fg='white', borderwidth=2, relief='groove')
etiqueta.place(x=60, y=80)

# Input para ingresar valor
caja_text = tk.Entry(ventana, width=20)
caja_text.place(x=180, y=80)

# Añadir los widgets a la ventana
boton = tk.Button(ventana, text='Buscar', command=buscar_pokemon)
boton.place(x=350, y=80)

# Crear etiquetas
nombre = tk.Label(ventana, text="")
nombre.place(x=60, y=120)

imagen = tk.Label(ventana)
imagen.place(x=60, y=140)

# Ejecutar el bucle de eventos
ventana.mainloop()
