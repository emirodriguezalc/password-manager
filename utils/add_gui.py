from tkinter import Canvas, PhotoImage, Label, Entry, Button, Frame, Tk
from utils.create_password import create_password
from utils.print_saved import print_saved
from utils.save import save_password_to_file
import os


def handle_save(addPasswords, email_entry, website_name_entry, website_url_entry, password_entry):
    save_password_to_file(
        email_entry, website_name_entry, website_url_entry, password_entry)
    addPasswords.destroy()

def destroy(addPasswords):
    addPasswords.destroy()


def add_gui(addPasswords):
    # Set up the main window
    addPasswords.config(padx=50, pady=50)

    # Create the canvas and add the logo
    canvas = Canvas(addPasswords, width=400, height=400)
    canvas.create_image(100, 100)
    canvas.grid(column=1, row=0)

    # Create the input frame
    input_frame = Frame(addPasswords)
    input_frame.grid(column=0, row=0, padx=10, pady=10)

    # Create the labels
    website_name_label = Label(input_frame, text="Website name:")
    website_name_label.grid(column=0, row=0, sticky="w")
    website_url_label = Label(input_frame, text="Website URL:")
    website_url_label.grid(column=0, row=1, sticky="w")
    email_label = Label(input_frame, text="Email/Username:")
    email_label.grid(column=0, row=2, sticky="w")
    password_label = Label(input_frame, text="Password:")
    password_label.grid(column=0, row=3, sticky="w")

    # Create the entry fields
    website_name_entry = Entry(input_frame, width=35)
    website_name_entry.grid(column=1, row=0)
    website_url_entry = Entry(input_frame, width=35)
    website_url_entry.grid(column=1, row=1)
    email_entry = Entry(input_frame, width=35)
    email_entry.grid(column=1, row=2)
    password_entry = Entry(input_frame, width=20)
    password_entry.grid(column=1, row=3)

    # Create the buttons
    generate_button = Button(input_frame, text="Generate Password",
                             command=lambda: create_password(password_entry))
    generate_button.grid(column=2, row=3, padx=10)
    add_button = Button(input_frame, text="Add",
                        command=lambda: handle_save(addPasswords, email_entry, website_name_entry, website_url_entry, password_entry))
    add_button.grid(column=1, row=4, columnspan=2, pady=10)
    print_button = Button(input_frame, text="Print saved", command=print_saved)
    print_button.grid(column=2, row=5, pady=10)
    print_button = Button(input_frame, text="Back", command=lambda: destroy(addPasswords))
    print_button.grid(column=2, row=6, pady=10)
