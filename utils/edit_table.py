import json
import os
from tkinter import Button, Frame, Label, messagebox, END, Entry, Tk


def destroy(viewPasswordsGui):
    viewPasswordsGui.destroy()


def edit_table(editPasswordsGui):
    # Clear the table
    editPasswordsGui.config(padx=50, pady=50)
    for widget in editPasswordsGui.winfo_children():
        widget.destroy()

    # Create the input frame
    input_frame = Frame(editPasswordsGui)
    input_frame.grid(column=0, row=0, padx=10, pady=10)

    # Create the table frame
    table_frame = Frame(editPasswordsGui)
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

    # Create the input fields and repopulate the table with updated data
    input_fields = []
    for i, password in enumerate(data):
        website_name_label = Label(
            table_frame, text=password['website_name'])
        website_name_label.grid(column=0, row=i+1, padx=5, pady=5)

        website_url_label = Label(
            table_frame, text=password['website_url'])
        website_url_label.grid(column=1, row=i+1, padx=5, pady=5)

        email_username_entry = Entry(table_frame)
        email_username_entry.insert(END, password['email'])
        email_username_entry.grid(column=2, row=i+1, padx=5, pady=5)
        input_fields.append(email_username_entry)

        password_entry = Entry(table_frame, show="*")
        password_entry.insert(END, password['password'])
        password_entry.grid(column=3, row=i+1, padx=5, pady=5)
        input_fields.append(password_entry)

    # Create the save button
    save_button = Button(input_frame, text="Save Changes",
                         command=lambda: save_changes(input_fields, data, editPasswordsGui))
    save_button.grid(column=2, row=2, pady=10)
    back_button = Button(input_frame, text="Back",
                         command=lambda: destroy(editPasswordsGui))
    back_button.grid(column=3, row=2, pady=10)

    return editPasswordsGui


def save_changes(input_fields, data, editPasswordsGui):
    # Update the data with the new input values
    for i in range(len(data)):
        data[i]['email'] = input_fields[i*2].get()
        data[i]['password'] = input_fields[i*2+1].get()

    # Save the updated data to the file
    with open('passwords_data.json', 'w') as fp:
        json.dump(data, fp)

    messagebox.showinfo("Success", "Changes saved successfully.")
    destroy(editPasswordsGui)
