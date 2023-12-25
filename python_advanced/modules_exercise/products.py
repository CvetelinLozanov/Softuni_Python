import json
import os
import tkinter as tk
from canvas import app
from helpers import clean_screen
#  Install Pillow library for this to work:
from PIL import Image, ImageTk

base_folder = os.path.dirname(__file__)


def update_current_user(username, product_id):
    with open('db/users.txt', 'r+', newline='\n') as f:
        users = [json.loads(u.strip()) for u in f]
        for user in users:
            if user['username'] == username:
                user['products'].append(product_id)
                f.seek(0)
                f.truncate()
                f.writelines([json.dumps(u) + '\n' for u in users])
                return


def purchase_product(product_id, is_available):
    with open('db/products.txt', 'r+') as f:
        products = [json.loads(p.strip()) for p in f]
        for product in products:
            if product['id'] == product_id:
                if product['count'] - 1 < 0:
                    is_available = False
                    render_products_screen(error=f"There is no quantity for selected {product['name']}")
                    return is_available
                product['count'] -= 1
                f.seek(0)
                f.truncate()
                f.writelines([json.dumps(p) + '\n' for p in products])
                return is_available


def buy_product(product_id):
    clean_screen()

    with open('db/current_user.txt', 'r') as file:
        username = file.read()

    is_product_available = True

    if username is not None:
        is_product_available = purchase_product(product_id, is_product_available)
        if is_product_available:
            update_current_user(username, product_id)
            render_products_screen()





def add_product(name, image, count):
    with open('db/products.txt', 'r+') as file:
        if name == '' or image == '' or count == '':
            render_add_product_screen(error='All fields are required!')
            return
        file.write(json.dumps({
            'id': len(file.readlines()) + 1,
            'name': name,
            'img_path': image,
            'count': count,
        }) + '\n')
    render_products_screen()


def render_add_product_screen(error=None):
    clean_screen()

    tk.Label(app, text='Name: ').grid(row=0, column=0)
    name = tk.Entry(app)
    name.grid(row=0, column=1)

    tk.Label(app, text='Image: ').grid(row=1, column=0)
    img = tk.Entry(app)
    img.grid(row=1, column=1)

    tk.Label(app, text='Count: ').grid(row=2, column=0)
    count = tk.Entry(app)
    count.grid(row=2, column=1)

    if error is not None:
        tk.Label(app, text=error).grid(row=4, column=0)

    tk.Button(app,
              text='Add',
              command=lambda: add_product(name.get(), img.get(), count.get())
              ).grid(row=3, column=0)

    tk.Button(app, text='Back', command=render_products_screen).grid(row=3, column=1)


def render_products_screen(error=None):
    clean_screen()

    with open('db/current_user.txt') as file:
        username = file.read()
    with (open('db/users.txt') as f):
        users = [json.loads(u.strip()) for u in f]
        for user in users:
            if user['username'] == username and user['is_admin']:
                tk.Label(app, text="Press the button if you want to add products:", wraplength=100, justify="center"
                         ).grid(row=0, column=0, pady=15)
                tk.Button(app,
                          text='Add product',
                          command=lambda: render_add_product_screen()
                          ).grid(row=0, column=1)
                break

    if error is not None:
        tk.Label(app, text=error).grid(row=0, column=3)

    with open('db/products.txt', 'r') as file:
        products = [json.loads(p.strip()) for p in file]
        for i, product in enumerate(products):
            row = i // 4 * 4 + 1
            column = i % 4
            tk.Label(app, text=product['name']).grid(row=row, column=column)

            img = Image.open(os.path.join(base_folder, 'db/images', product['img_path'])).resize((100, 100))
            photo_image = ImageTk.PhotoImage(img)
            image_label = tk.Label(image=photo_image)
            image_label.image = photo_image
            image_label.grid(row=row + 1, column=column)

            tk.Label(app, text=product["count"]).grid(row=row + 2, column=column)
            tk.Button(app,
                      text=f"Buy {product['id']}",
                      command=lambda p=product['id']: buy_product(p)
                      ).grid(row=row + 3, column=column)
