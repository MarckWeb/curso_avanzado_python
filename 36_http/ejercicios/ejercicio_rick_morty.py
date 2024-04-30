import tkinter as tk
import requests
from PIL import Image, ImageTk
import io


class RickAndMortyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rick and Morty Character Viewer")
        self.root.geometry("500x500")  # Establecer el tamaño de la ventana

        self.label = tk.Label(root, text="Enter character ID:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(
            root, text="Show Character", command=self.show_character)
        self.button.pack()

        self.image_label = tk.Label(root)
        self.image_label.pack()

    def fetch_character_info(self, character_id):
        url = f"https://rickandmortyapi.com/api/character/{character_id}"
        response = requests.get(url)
        character_data = response.json()
        return character_data

    def show_character(self):
        character_id = self.entry.get()
        character_data = self.fetch_character_info(character_id)

        if 'error' in character_data:
            self.image_label.config(text="Character not found")
            return

        image_url = character_data['image']
        image_data = requests.get(image_url).content
        image = Image.open(io.BytesIO(image_data))
        photo = ImageTk.PhotoImage(image)

        self.image_label.config(image=photo)
        self.image_label.image = photo


def main():
    root = tk.Tk()
    app = RickAndMortyApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
