import json
import os
from tkinter import Button, Frame, Label, messagebox, END, Entry, Tk


def update_table(viewPasswordsGui, on_add_button_click):
    # Clear the table

    viewPasswordsGui.config(padx=50, pady=50)
    for widget in viewPasswordsGui.winfo_children():
        widget.destroy()

    # Create the input frame
    input_frame = Frame(viewPasswordsGui)
    input_frame.grid(column=0, row=0, padx=10, pady=10)

    # Create the table frame
    table_frame = Frame(viewPasswordsGui)
    table_frame.grid(column=0, row=1, padx=10, pady=10)

    # Create table headers
    website_name_header = Label(
        table_frame, text="WEBSITE NAME", font=("Arial Bold", 12))
    website_name_header.grid(column=0, row=0, padx=5, pady=5)
    website_url_header = Label(
        table_frame, text="WEBSITE URL", font=("Arial Bold", 12))
    website_url_header.grid(column=1, row=0, padx=5, pady=5)
    email_username_header = Label(
        table_frame, text="EMAIL/USERNAME", font=("Arial Bold", 12))
    email_username_header.grid(column=2, row=0, padx=5, pady=5)
    password_header = Label(
        table_frame, text="PASSWORD", font=("Arial Bold", 12))
    password_header.grid(column=3, row=0, padx=5, pady=5)

    file_name = 'passwords_data.json'
    if os.path.exists(file_name):
        with open('passwords_data.json', 'r') as fp:
            data = json.load(fp)

    # Repopulate the table with updated data
    for i, password in enumerate(data):
        website_name_label = Label(
            table_frame, text=password['website_name'])
        website_name_label.grid(column=0, row=i+1, padx=5, pady=5)

        website_url_label = Label(
            table_frame, text=password['website_url'])
        website_url_label.grid(column=1, row=i+1, padx=5, pady=5)

        email_username_label = Label(
            table_frame, text=password['email'])
        email_username_label.grid(column=2, row=i+1, padx=5, pady=5)

        password_entry = password['password']
        password_label = Label(
            table_frame, text=password['password'])
        password_label.grid(column=3, row=i+1, padx=5, pady=5)
    # Create buttons to copy URL and password to clipboard
        copy_url_button = Button(
            table_frame, text="Copy URL", command=lambda url=password['website_url']: viewPasswordsGui.clipboard_append(url))
        copy_url_button.grid(column=4, row=i+1, padx=5, pady=5)

        copy_password_button = Button(
            table_frame, text="Copy Password", command=lambda password=password_entry: viewPasswordsGui.clipboard_append(password))
        copy_password_button.grid(column=5, row=i+1, padx=5, pady=5)

    add_password_button = Button(
        viewPasswordsGui, text="Add new password", command=on_add_button_click)
    add_password_button.grid(column=2, row=5, pady=10)
    return viewPasswordsGui
