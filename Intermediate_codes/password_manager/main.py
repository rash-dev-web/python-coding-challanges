from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


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
    # changed the file format to json in write mode
    website = website_textbox.get()
    email_username = email_username_textbox.get()
    password = password_textbox.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }
    }

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Empty field", message="Don't leave any field blank")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # write to the data file
                # added the json code to read and write data into json file
                json.dump(data, data_file, indent=4)
                # is_ok = messagebox.askokcancel(title="Confirm", message=f"These are the details:\nWebsite:" f" {
                # website}\nEmail/Username: {email_username}\n" f"Password: {password}\nIs it ok to save?") if is_ok:
                # file.write(f"{website} | {email_username} | {password} \n")
        finally:
            website_textbox.delete(0, END)
            password_textbox.delete(0, END)


# ---------------------------- search password ---------------------------#
def search_password():
    # get the website
    website = website_textbox.get()
    if len(website) == 0:
        messagebox.showwarning(title="Input field", message="Please enter a search term")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
            # print(data)
        except FileNotFoundError:
            messagebox.showwarning(title="Error", message="No data file Found")
        else:
            try:
                website_data = data[website]
            except KeyError:
                # this block of code can be done with if else
                messagebox.showwarning(title="Error", message=f"No details for the {website} exists.")
            else:
                messagebox.showinfo(title=website, message=f"Your email: {website_data['email']}\n"
                                                           f"Your Password: {website_data['password']}")


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

# search button
search_button = Button(text="Search", width=15, command=search_password)
search_button.grid(column=2, row=1)

# generate password button
generate_pwd_button = Button(text="Generate Password", command=generate_password)
generate_pwd_button.grid(column=2, row=3)

# add button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
