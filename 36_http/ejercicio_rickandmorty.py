import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO


def mostrar_personajes(event):
    try:
        respuesta = requests.get("https://rickandmortyapi.com/api/character")
        datos = respuesta.json()['results']
        columna = 0
        fila = 0
        for item in datos:
            url_imagen = item['image']
            imagen_response = requests.get(url_imagen)
            # Estado de la respuesta
            print("Estado de la respuesta:", imagen_response.status_code)
            imagen_data = imagen_response.content
            # Tamaño de los datos de la imagen
            print("Tamaño de los datos de la imagen:", len(imagen_data))
            imagen = Image.open(BytesIO(imagen_data))
            imagen = imagen.resize((100, 100))
            foto = ImageTk.PhotoImage(imagen)
            etiqueta = tk.Label(ventana, image=foto)
            etiqueta.image = foto
            etiqueta.grid(row=fila, column=columna)
            columna += 1
            if columna == 4:
                fila += 1
                columna = 0
    except requests.RequestException as e:
        print("Ha ocurrido un error de solicitud:", e)


ventana = tk.Tk()
ventana.title("Personajes Rick and Morty")
ventana.geometry("500x500")
ventana.bind("<Enter>", mostrar_personajes)

ventana.mainloop()
