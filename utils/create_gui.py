from tkinter import Canvas, PhotoImage, Label, Entry, Button
from utils.create_password import create_password
from utils.print_saved import print_saved
from utils.save import save_password_to_file


def create_gui(root):
    # Set up the main window
    root.config(padx=50, pady=50)

    # Create the canvas and add the logo
    canvas = Canvas(width=400, height=400)
    photo = PhotoImage(file='./wolf.png')
    canvas.create_image(100, 100, image=photo)
    canvas.grid(column=1, row=0)

    # Create the labels
    website_name_label = Label(text="Website name:")
    website_name_label.grid(column=0, row=1)
    website_url_label = Label(text="Website URL:")
    website_url_label.grid(column=0, row=2)
    email_label = Label(text="Email/Username:")
    email_label.grid(column=0, row=3)
    password_label = Label(text="Password:")
    password_label.grid(column=0, row=4)

    # Create the entry fields
    website_name_entry = Entry(width=35)
    website_name_entry.grid(column=1, row=1, columnspan=2)
    website_url_entry = Entry(width=35)
    website_url_entry.grid(column=1, row=2, columnspan=2)
    email_entry = Entry(width=35)
    email_entry.grid(column=1, row=3, columnspan=2)
    password_entry = Entry(width=20)
    password_entry.grid(column=1, row=4)

    # Create the buttons
    generate_button = Button(text="Generate Password",
                             command=lambda: create_password(password_entry))
    generate_button.grid(column=2, row=4)
    add_button = Button(text="Add", command=lambda: save_password_to_file(
        email_entry, website_name_entry, website_url_entry, password_entry))
    add_button.grid(column=1, row=5, columnspan=2)
    print_button = Button(text="Print saved", command=print_saved)
    print_button.grid(column=2, row=6)
