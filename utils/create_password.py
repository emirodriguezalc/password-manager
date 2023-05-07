import json
import os
from tkinter import Canvas, Tk, PhotoImage, Label, Entry, Button, messagebox, END
import string
from secrets import choice
# ---------- CREATE PASSWORD ---------- #

# necessary imports
import secrets
import string

from utils.save import save


def create_password(password_entry):

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
