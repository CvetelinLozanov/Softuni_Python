import tkinter as tk


def create_app():
    root = tk.Tk()
    root.title('GUI Product Shop')
    root.geometry('700x600+0+0')
    # root.grid_columnconfigure(0, weight=1)
    # root.grid_columnconfigure(1, weight=1)
    # root.grid_columnconfigure(2, weight=1)
    # root.grid_columnconfigure(3, weight=1)
    return root


app = create_app()
