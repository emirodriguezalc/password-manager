import json
import os
from tkinter import Canvas, Tk, PhotoImage, Label, Entry, Button, messagebox, END
import string
from secrets import choice
# ---------- SAVE PASSWORD ---------- #


def save(email_entry, website_name_entry, website_url_entry, password_entry):
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
