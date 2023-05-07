from tkinter import Tk, messagebox, Label, Entry, Button
from utils.authenticate import authenticate
from utils.create_gui import create_gui
from utils.register import register

USERS_FILE = "users.json"

def login_window():
    login_root = Tk()
    login_root.title("Login")

    def login_command():
        login(username_entry.get(), password_entry.get())

    def register_window():
        register_root = Tk()
        register_root.title("Register")

        def register_command():
            register_user(username_entry.get(), password_entry.get())
            register_root.destroy()

        username_label = Label(register_root, text="Username")
        username_label.pack()
        username_entry = Entry(register_root)
        username_entry.pack()

        password_label = Label(register_root, text="Password")
        password_label.pack()
        password_entry = Entry(register_root, show="*")
        password_entry.pack()

        register_button = Button(
            register_root, text="Register", command=register_command)
        register_button.pack()

    username_label = Label(login_root, text="Username")
    username_label.pack()
    username_entry = Entry(login_root)
    username_entry.pack()

    password_label = Label(login_root, text="Password")
    password_label.pack()
    password_entry = Entry(login_root, show="*")
    password_entry.pack()

    login_button = Button(login_root, text="Login", command=login_command)
    login_button.pack()

    register_button = Button(
        login_root, text="Register", command=register_window)
    register_button.pack()

    login_root.mainloop()


def login(username, password):
    if authenticate(username, password, USERS_FILE):
        main()
    else:
        messagebox.showerror("Error", "Invalid username or password")


def register_user(username, password):
    if register(username, password, USERS_FILE):
        messagebox.showinfo("Success", "User registered successfully")
    else:
        messagebox.showerror("Error", "Username already taken")


def main():
    root = Tk()
    root.title("She wolf password manager")

    create_gui(root)

    root.mainloop()


if __name__ == "__main__":
    login_window()
