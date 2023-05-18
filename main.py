from tkinter import *
import pandas as pd
import random
import sys

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

random_italian_word = None
random_spanish_word = None

try:
    df = pd.read_csv("data/italian_words.csv")
except FileNotFoundError:
    print("no file")
    sys.exit()
else:
    if not df.empty:
        words_dict = df.to_dict()
        random_index = random.randint(0, len(words_dict["Italian"].values()))
        random_italian_word = words_dict["Italian"][random_index]
        random_spanish_word = words_dict["Spanish"][random_index]


def flip_card():
    # Si la carta tiene como título 'Italian', entonces lo cambio al español y viceversa
    if canvas.itemcget(card_title, "text").title() == "Italian":
        window.after_cancel(call_id)
        canvas.itemconfig(card_background, image=card_back)
        canvas.itemconfig(card_title, text="Spanish", fill="white")
        canvas.itemconfig(card_word, text=random_spanish_word, fill="white")
    else:
        window.after(3000)
        canvas.itemconfig(card_background, image=card_front)
        canvas.itemconfig(card_title, text="Italian", fill="black")


def right_button_pressed():
    pass


def change_word():
    global random_italian_word, random_spanish_word

    if canvas.itemcget(card_title, "text").title() == "Spanish":
        index = random.randint(0, len(words_dict["Italian"].values()))
        random_italian_word = words_dict["Italian"][index]
        random_spanish_word = words_dict["Spanish"][index]
        canvas.itemconfig(card_background, image=card_front)
        canvas.itemconfig(card_title, text="Italian", fill="black")
        canvas.itemconfig(card_word, text=random_italian_word, fill="black")
        window.after(3000, flip_card)


def show_warning():
    canvas.itemconfig(card_title, text="No language available", fill="red")
    canvas.itemconfig(card_word, text="Missing file", fill="red")


# ------------------------ UI SETTINGS ------------------------
# Window
window = Tk()
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
window.title("Flashy - by iPalazzolo")
window.resizable(False, False)

call_id = window.after(3000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)

card_title = canvas.create_text(400, 150, text="Italian", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text=random_italian_word, font=("Arial", 60, "bold"))

# Right & Wrong Buttons
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_img, highlightthickness=0, command=right_button_pressed)
right_button.grid(column=0, row=1)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=change_word)
wrong_button.grid(column=1, row=1)


window.mainloop()
