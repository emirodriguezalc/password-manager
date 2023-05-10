import json
import os
import tkinter as tk
from tkinter import Button, Frame, Label, messagebox, END, Entry, Tk
from utils.add_gui import add_gui
from utils.edit_table import edit_table
from utils.update_table import update_table


def view_passwords_gui(viewPasswordsGui, file_name):
    # Set up the main window
    viewPasswordsGui.config(padx=50, pady=50)

    def on_add_button_click():
        viewPasswordsGui.view_b = tk.Toplevel(viewPasswordsGui)
        add_gui(viewPasswordsGui.view_b, file_name)
        viewPasswordsGui.wait_window(viewPasswordsGui.view_b)
        update_table(viewPasswordsGui, on_add_button_click, on_edit_button_click, file_name) #Update the table

    def on_edit_button_click():
        viewPasswordsGui.view_c = tk.Toplevel(viewPasswordsGui)
        edit_table(viewPasswordsGui.view_c, file_name)
        viewPasswordsGui.wait_window(viewPasswordsGui.view_c)
        update_table(viewPasswordsGui, on_add_button_click, on_edit_button_click, file_name) #Update the table

    # Create the "EDIT" button

    update_table(viewPasswordsGui, on_add_button_click, on_edit_button_click, file_name)
