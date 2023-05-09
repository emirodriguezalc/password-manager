import json
import os
import tkinter as tk
from tkinter import Button, Frame, Label, messagebox, END, Entry, Tk
from utils.add_gui import add_gui
from utils.save import save_password_to_file
from utils.update_table import update_table


def view_passwords_gui(viewPasswordsGui):
    # Set up the main window
    viewPasswordsGui.config(padx=50, pady=50)

    def on_add_button_click():
        viewPasswordsGui.view_b = tk.Toplevel(viewPasswordsGui)
        add_gui(viewPasswordsGui.view_b)
        viewPasswordsGui.wait_window(viewPasswordsGui.view_b)
        update_table(viewPasswordsGui, on_add_button_click)

    update_table(viewPasswordsGui, on_add_button_click)
