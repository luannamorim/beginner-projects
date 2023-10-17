import qrcode
import tkinter as tk
from tkinter import filedialog
from datetime import datetime


data = input('Link QRCODE: ')
name = datetime.now()
formatted_name = name.strftime("%Y%m%d-%H%M%S")

root = tk.Tk()
dirNome = filedialog.askdirectory(
    parent=root, initialdir="/", title='Select the folder')

img = qrcode.make(data)
file_path = f"{dirNome}/{formatted_name}.png"
img.save(file_path)

print(f'QRCODE saved successfully at: {file_path}')