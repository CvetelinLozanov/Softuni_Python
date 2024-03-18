import tkinter as tk
from tkinter import messagebox
import random


class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")

        self.categories = {
            "Animals": ["cat", "dog", "elephant", "giraffe", "monkey"],
            "Countries": ["india", "japan", "brazil", "australia", "bulgaria"],
            "Fruits": ["apple", "banana", "orange", "grape", "kiwi"]
        }
        self.current_category = tk.StringVar()
        self.secret_word = ""
        self.guesses_left = 6
        self.guesses = set()

        master.geometry("650x650")
        self.canvas = tk.Canvas(master, width=400, height=400, bg="black")
        self.canvas.pack(anchor=tk.CENTER, expand=True)

        self.category_label = tk.Label(master, text="Category: ")
        self.category_label.pack()

        self.word_display = tk.Label(master, text="", font=("Helvetica", 20))
        self.word_display.pack()

        self.label = tk.Label(master, text="Guess a letter:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.wrong_letter_size = tk.Label(master, text="")
        self.wrong_letter_size.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.guess_letter)
        self.guess_button.pack(pady=5)

        self.new_word_button = tk.Button(master, text="New Word", command=self.choose_new_word)
        self.new_word_button.pack(pady=5)

        self.choose_category()
        self.draw_gallows()

    def choose_category(self):
        # This method should allow the player to choose a category and set the current_category attribute
        categories = list(self.categories.keys())
        self.current_category.set(categories[0])
        drop_down_menu = tk.OptionMenu(self.master, self.current_category, *categories)
        drop_down_menu.pack(pady=5)

    def choose_new_word(self):
        # This method should choose a new word from the selected category and reset the game attributes
        self.restart()
        current_category = self.current_category.get()
        self.category_label.configure(text=f"Category: {current_category}")
        word_from_category = random.choice(self.categories[current_category])
        self.word_display.configure(text=f"{word_from_category[0]}{' _ ' * (len(word_from_category) - 2)}"
                                         f"{word_from_category[-1]}")
        self.secret_word = word_from_category

    def restart(self):
        self.canvas.delete("all")
        self.draw_gallows()
        self.guesses_left = 6

    def draw_head(self, x, y, r, width, canvas, color='grey'):  # center coordinates, radius
        x0 = x - r
        y0 = y - r
        x1 = x + r
        y1 = y + r
        canvas.create_oval(x0, y0, x1, y1, width=width, outline=color)
        canvas.pack()

    def create_line(self, x0, y0, x1, y1, width, canvas, dotted=None):
        canvas.create_line(x0, y0, x1, y1, width=width, fill='grey', dash=dotted)
        canvas.pack()

    def draw_gallows(self):
        self.create_line(100, 25, 100, 400, 10, self.canvas)
        self.create_line(95, 25, 254, 25, 10, self.canvas)
        self.create_line(100, 90, 165, 25, 10, self.canvas)
        self.draw_rope(250, 25, 250, 70, 8)

    def draw_rope(self, x0: int, y0: int, x1: int, y1: int, width: int):
        self.create_line(x0, y0, x1, y1, width, self.canvas, (2,))

    def draw_body(self, x0: int, y0: int, x1: int, y1: int, width: int):
        self.create_line(x0, y0, x1, y1, width, self.canvas)

    def draw_left_arm(self, x0: int, y0: int, x1: int, y1: int, width: int):
        self.create_line(x0, y0, x1, y1, width, self.canvas)

    def draw_right_arm(self, x0: int, y0: int, x1: int, y1: int, width: int):
        self.create_line(x0, y0, x1, y1, width, self.canvas)

    def draw_left_leg(self, x0: int, y0: int, x1: int, y1: int, width: int):
        self.create_line(x0, y0, x1, y1, width, self.canvas)

    def draw_right_leg(self, x0: int, y0: int, x1: int, y1: int, width: int):
        self.create_line(x0, y0, x1, y1, width, self.canvas)

    def draw_hangman(self):
        # This method should draw the hangman based on the number of incorrect guesses
        if self.guesses_left <= 5:
            self.draw_head(250, 100, 30, 5, self.canvas)
            if self.guesses_left <= 4:
                self.draw_body(250, 130, 250, 250, 5)
                if self.guesses_left <= 3:
                    self.draw_left_arm(200, 150, 250, 180, 5)
                    if self.guesses_left <= 2:
                        self.draw_right_arm(250, 180, 300, 150, 5)
                        if self.guesses_left <= 1:
                            self.draw_right_leg(300, 280, 250, 250, 5)
                            if self.guesses_left == 0:
                                self.draw_left_leg(200, 280, 250, 250, 5)

    def guess_letter(self):
        # This method should handle the player's guess and update the game state accordingly
        chosen_letter = self.entry.get()
        if len(chosen_letter) > 1:
            self.wrong_letter_size.configure(text="You have entered too long text. Please enter one letter!", fg='red')
            return

        self.wrong_letter_size.configure(text='')

        if chosen_letter in self.secret_word:
            pass
        else:
            self.guesses_left -= 1
            self.draw_hangman()

    def update_word_display(self):
        # This method should update the displayed word with the guessed letters
        pass


def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
