import json
import os
from typing import Dict
from tkinter import messagebox, END, Entry


def save_password_to_file(email_entry: Entry, website_name_entry: Entry, website_url_entry: Entry, password_entry: Entry) -> None:
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
            with open(file_name, 'a') as f:
                f.write(json.dumps(data_to_save) + '\n')
                clear_form_entries(website_name_entry, website_url_entry, password_entry)

def clear_form_entries(website_name_entry: Entry, website_url_entry: Entry, password_entry: Entry) -> None:
    website_name_entry.delete(0, END)
    website_url_entry.delete(0, END)
    password_entry.delete(0, END)
