import qrcode
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
dirNome = filedialog.askdirectory(
    parent=root, initialdir="/", title='Select the folder')

data = input('Link QRCODE: ')
name = input('Name QRCODE: ')

img = qrcode.make(data)
file_path = f"{dirNome}/{name}.png"
img.save(file_path)

print(f'QRCODE saved successfully at: {file_path}')
