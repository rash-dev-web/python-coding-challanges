from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_textbox.insert(0, password)
    pyperclip.copy(password)

    # print(f"Your password is: {password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("data.txt", "a") as file:
        website = website_textbox.get()
        email_username = email_username_textbox.get()
        password = password_textbox.get()

        if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
            messagebox.showwarning(title="Empty field", message="Don't leave any field blank")
        else:
            is_ok = messagebox.askokcancel(title="Confirm", message=f"These are the details:\nWebsite:"
                                                                    f" {website}\nEmail/Username: {email_username}\n"
                                                                    f"Password: {password}\nIs it ok to save?")
            if is_ok:
                file.write(f"{website} | {email_username} | {password} \n")
                website_textbox.delete(0, END)
                password_textbox.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

# website entry
website_textbox = Entry(width=35)
website_textbox.grid(column=1, row=1, columnspan=2)
website_textbox.focus()

# email username label
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

# email/username entry
email_username_textbox = Entry(width=35)
email_username_textbox.grid(column=1, row=2, columnspan=2)
email_username_textbox.insert(0, "rahseed.m@live.com")

# password label
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# email/username entry
password_textbox = Entry(width=21)
password_textbox.grid(column=1, row=3)

# generate password button
generate_pwd_button = Button(text="Generate Password", command=generate_password)
generate_pwd_button.grid(column=2, row=3)

# add button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
