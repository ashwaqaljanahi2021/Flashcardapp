from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
# Functionality
try:
    data = pandas.read_csv("words_to_learn.csv")
    english_data = data["English"].to_list()
    french_data = data["French"].to_list()
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    english_data = data["English"].to_list()
    french_data = data["French"].to_list()

CURRENT = 0
english_words = english_data
french_words = french_data
words_to_learn = {
    "English": english_words,
    "French": french_words
}

def turn():
    card2.grid(column=2, row=1, columnspan=2)
def to_learn():
    global CURRENT
    words_to_learn["English"] = english_words
    words_to_learn["French"] = french_words
    pandas.DataFrame(words_to_learn).to_csv("words_to_learn.csv")
    CURRENT += 1
    card = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
    card.create_image(400, 300, image=card_back)
    card.grid(column=2, row=1, columnspan=2)
    card.create_text(400, 200, text="English", font=("Arial", 35, "italic"))
    card.create_text(400, 300, text=f"{english_data[CURRENT]}", font=("Arial", 40, "bold"))

    def turn2():
        card2.grid(column=2, row=1, columnspan=2)

    card.after(3000, turn2)
    card2 = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
    card2.create_image(400, 300, image=card_front)
    card2.create_text(400, 200, text="French", font=("Arial", 35, "italic"), fill="black")
    card2.create_text(400, 300, text=f"{french_data[CURRENT]}", font=("Arial", 40, "bold"), fill="black")


def turn_back():
    global CURRENT
    english_words.remove(english_data[CURRENT])
    french_words.remove(french_data[CURRENT])
    CURRENT += 1

    card = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
    card.create_image(400, 300, image=card_back)
    card.grid(column=2, row=1, columnspan=2)
    card.create_text(400, 200, text="English", font=("Arial", 35, "italic"))
    card.create_text(400, 300, text=f"{english_data[CURRENT]}", font=("Arial", 40, "bold"))

    def turn2():
        card2.grid(column=2, row=1, columnspan=2)

    card.after(3000, turn2)
    card2 = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
    card2.create_image(400, 300, image=card_front)
    card2.create_text(400, 200, text="French", font=("Arial", 35, "italic"), fill="black")
    card2.create_text(400, 300, text=f"{french_data[CURRENT]}", font=("Arial", 40, "bold"), fill="black")


# UI Setup
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flash Cards App")

# card on the back

card = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back = PhotoImage(file="images/card_back.png")
card.create_image(400, 300, image=card_back)
card.grid(column=2, row=1, columnspan=2)
card.create_text(400, 200, text="English", font=("Arial", 35, "italic"))
card.create_text(400, 300, text=f"{english_data[CURRENT]}", font=("Arial", 40, "bold"))
card.after(3000, turn)

card2 = Canvas(width=800, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card2.create_image(400, 300, image=card_front)
card2.create_text(400, 200, text="French", font=("Arial", 35, "italic"), fill="black")
card2.create_text(400, 300, text=f"{french_data[CURRENT]}", font=("Arial", 40, "bold"), fill="black")

# Wrong Button
x_image = PhotoImage(file="images/wrong.png")
wrong = Button(width=100, height=100, bg=BACKGROUND_COLOR, image=x_image, highlightthickness=0,
               highlightbackground=BACKGROUND_COLOR, command=to_learn)
wrong.grid(column=2, row=4, columnspan=1)

# Right Button
check_image = PhotoImage(file="images/right.png")
right = Button(width=100, height=100, bg=BACKGROUND_COLOR, image=check_image, highlightthickness=0,
               highlightbackground=BACKGROUND_COLOR, command=turn_back)
right.grid(column=3, row=4, columnspan=1)

window.mainloop()
