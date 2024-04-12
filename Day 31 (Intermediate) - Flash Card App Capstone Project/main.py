from tkinter import *
import pandas
import random

# ------------------------------------CONSTANTS---------------------------#
BACKGROUND_COLOR = "#B1DDC6"

# ------------------------------------GLOBAL VARIABLES--------------------#
current_card = {}
words_to_learn = pandas.DataFrame(columns=["French", "English"])

# ------------------------------------NEXT CARD---------------------------#
try:
    words_to_learn = pandas.read_csv("data/words_to_learn.csv")
except:
    data = pandas.read_csv("data/french_words.csv")
    data.to_csv("data/words_to_learn.csv", index=False)
    words_to_learn = pandas.read_csv("data/words_to_learn.csv")
finally:
    to_learn = words_to_learn.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    if flip_timer is not None:
        window.after_cancel(flip_timer)
    canvas.itemconfig(image_container, image=card_front)
    try:
        current_card = random.choice(to_learn)
    except IndexError:
        canvas.itemconfig(language_text, text="No cards remain.", fill="black")
        canvas.itemconfig(word_text, text="You finished!", fill="black")
    else:
        canvas.itemconfig(language_text, text="French", fill="black")
        canvas.itemconfig(word_text, text=current_card["French"], fill="black")
        flip_timer = window.after(3000, flip_card)


# -----------------------------------FLIP CARD----------------------------#
def flip_card():
    canvas.itemconfig(image_container, image=card_back)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


# -----------------------------------UPDATE DICTIONARY---------------------#
def update_dict():
    global to_learn
    try:
        to_learn.remove(current_card)
    except ValueError:
        pass
    else:
        # Update the "words_to_learn.csv" with the completed dictionary (only shows after program end)
        pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)

# -----------------------------------UI-----------------------------------#


# Window setup.
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas setup.
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Card setup.
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
image_container = canvas.create_image(400, 263, image=card_front)

# Text.
language_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
flip_timer = window.after(3000, flip_card)
next_card()

# Button setup.
check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=lambda: [next_card(), update_dict()])
check_button.grid(row=1, column=1)

unknown_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

window.mainloop()
