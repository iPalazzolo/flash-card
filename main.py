from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"


def read_data():
    try:
        df_it_words = pd.read_csv("data/italian_words.csv")
    except FileNotFoundError:
        show_warning()
    else:
        if not df_it_words.empty:
            for index, row in df_it_words.iterrows():
                italian_words.append(row[0])
                spanish_words.append(row[1])


italian_words = []
spanish_words = []
read_data()

random_italian_word = random.choice(italian_words)
random_spanish_word = spanish_words[italian_words.index(random_italian_word)]


def flip_card():
    window.after_cancel(call_id)
    # Si la carta tiene como título 'Italian', entonces lo cambio al español y viceversa
    if canvas.itemcget(card_title, "text").title() == "Italian":
        canvas.itemconfig(card_background, image=card_back)
        canvas.itemconfig(card_title, text="Spanish", fill="white")
        canvas.itemconfig(card_word, text=random_spanish_word, fill="white")
    else:
        canvas.itemconfig(card_background, image=card_front)
        canvas.itemconfig(card_title, text="Italian", fill="black")
        change_word()


def change_word():
    global random_italian_word
    global random_spanish_word

    random_italian_word = random.choice(italian_words)
    random_spanish_word = spanish_words[italian_words.index(random_italian_word)]
    canvas.itemconfig(card_word, text=random_italian_word)


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

right_button = Button(image=right_img, highlightthickness=0, command=change_word)
right_button.grid(column=0, row=1)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=change_word)
wrong_button.grid(column=1, row=1)


window.mainloop()
