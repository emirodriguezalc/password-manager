import json
import os
from tkinter import Canvas, Tk, PhotoImage, Label, Entry, Button, messagebox, END
import string
from secrets import choice
from utils.create_password import create_password
from utils.save import save
from utils.print_saved import print_saved

# ---------- GUI ---------- #
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
generate_button = Button(text="Generate Password",
                         command=lambda: create_password(password_entry))
generate_button.grid(column=2, row=5)
add_button = Button(text="Add", command=lambda: save(
    email_entry, website_name_entry, website_url_entry, password_entry))
add_button.grid(column=1, row=6, columnspan=2)
print_button = Button(text="Print saved", command=print_saved)
print_button.grid(column=3, row=7)

screen.mainloop()
