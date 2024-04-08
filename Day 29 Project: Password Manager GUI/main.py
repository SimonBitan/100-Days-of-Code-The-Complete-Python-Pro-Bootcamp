from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = letter_list + number_list + symbol_list
    shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if website == "" or username == "" or password == "":
        messagebox.showinfo(title="Error", message="Please ensure no field is empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail/Username: {username} "
                                                  f"\nPassword: {password} \nOk to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {username} | {password}\n")
            # Clear the input fields.
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


# Window setup.
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas setup.
canvas = Canvas(width=200, height=200)
canvas.grid(row=0, column=1)

# Image setup.
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)

# Labels.
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Input fields.
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="w")
website_input.focus()

username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2, sticky="w")
username_input.insert(0, "example@gmail.com")

password_input = Entry(width=35)
password_input.grid(row=3, column=1, sticky="w")

# Buttons.
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(row=3, column=2, sticky="w")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="w", pady=20)

# Keep window open.
window.mainloop()
