import tkinter as tk
from pystray import Icon as icon, MenuItem as item
from PIL import Image
import keyboard
import threading

def create_window():
    def on_ok():
        text = "\n" + text_box.get("1.0", tk.END)
        with open(r"c:\Soft\Obsidian\ObsDataBase\1\004 INBOX.md", "a", encoding='utf-8') as file:
            file.write(text)
        window.destroy()

    window = tk.Tk()
    window.title("Быстрая заметка")
    window.attributes('-topmost', True)

    window.after(1, lambda: window.focus_force())

    text_box = tk.Text(window, height=10, width=50)
    text_box.pack()
    text_box.after(1, lambda: text_box.focus())

    window.bind('<Return>', lambda event: on_ok())

    tk.Button(window, text="OK", command=on_ok).pack(side=tk.LEFT)
    tk.Button(window, text="Отмена", command=window.destroy).pack(side=tk.RIGHT)

    window.mainloop()

def on_hotkey():
    create_window()

def setup(icon):
    icon.visible = True
    keyboard.add_hotkey('win+shift', on_hotkey)

def run_script():
    image = Image.open("icon.ico")  # Укажите путь к вашей иконке
    icon('Test', image, menu=(item('Выход', lambda: exit(0)),)).run(setup)

threading.Thread(target=run_script).start()
