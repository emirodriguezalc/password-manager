from tkinter import END
import string
import random

def create_password(password_entry_widget):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars

    pwd_length = 12

    while True:
        pwd = ''.join(random.choices(alphabet, k=pwd_length))
        if all(char not in letters for char in pwd):
            continue
        if all(char not in special_chars for char in pwd):
            continue
        if sum(char in digits for char in pwd) < 2:
            continue
        break

    password_entry_widget.delete(0, END)
    password_entry_widget.insert(END, pwd)
