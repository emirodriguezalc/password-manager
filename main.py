import json
import os
from tkinter import Canvas, Tk, PhotoImage, Label, Entry, Button, messagebox, END
import string
from secrets import choice

# ---------- CREATE PASSWORD ---------- #

# necessary imports
import secrets
import string


def create_password():

    # define the alphabet
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    alphabet = letters + digits + special_chars

    # fix password length
    pwd_length = 12

    # generate password meeting constraints
    while True:
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))

        if (any(char in special_chars for char in pwd) and
                sum(char in digits for char in pwd) >= 2):
            break
    password_entry.delete(0, END)
    password_entry.insert(END, pwd)
    password_entry.clipboard_append(pwd)


# ---------- SAVE PASSWORD ---------- #

def save():
    email = email_entry.get()
    website_name = website_name_entry.get()
    website_url = website_url_entry.get()
    password = password_entry.get()
    if len(website_url) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please fill all fields")
    else:
        is_ok = messagebox.askokcancel(
            title=website_name, message=f"You've entered\nEmail: {email}\nPassword: {password}\n"f"Are you sure you want to save?")
        if is_ok:
            data_to_save = {
                "email": email,
                "website_name": website_name,
                "website_url": website_url,
                "password": password,
            }
            file_name = 'passwords_data.json'
            if not os.path.exists(file_name):
                with open(file_name, 'w') as f:
                    json.dump([], f)
            with open(file_name, 'r') as f:
                data = json.load(f)
            data.append(data_to_save)
            with open(file_name, 'w') as f:
                json.dump(data, f)
                website_name_entry.delete(0, END)
                website_url_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------- GUI ---------- #


def print_saved():
    with open('passwords_data.json', 'r') as fp:
        data = json.load(fp)
        print(data)


screen = Tk()
screen.config(padx=50, pady=50)
screen.title("She wolf password manager")
canvas = Canvas(width=400, height=400)
photo = PhotoImage(file='wolf.png')
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)
# Allow users to store their website name, website URL, username, and password for each account.

# Labels
website_name = Label(text="Website name: ")
website_name.grid(column=0, row=1)

website_url = Label(text="Website URL: ")
website_url.grid(column=0, row=2)

email = Label(text="Email/Username: ")
email.grid(column=0, row=3)

password = Label(text="Password")
password.grid(column=0, row=4)

# Entries
website_name_entry = Entry(width=35)
website_name_entry.grid(column=1, row=1, columnspan=2)

website_url_entry = Entry(width=35)
website_url_entry.grid(column=1, row=2, columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=3, columnspan=2)
password_entry = Entry(width=20)
password_entry.grid(column=1, row=4)

# Buttons
generate_button = Button(text="Generate Password", command=create_password)
generate_button.grid(column=2, row=5)
add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=6, columnspan=2)
print_button = Button(text="Print saved", command=print_saved)
print_button.grid(column=3, row=7)

screen.mainloop()
