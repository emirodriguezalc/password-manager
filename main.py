from tkinter import Tk
from utils.create_gui import create_gui

# Main function


def main():
    # Create the main window
    root = Tk()
    root.title("She wolf password manager")

    # Create the GUI
    create_gui(root)

    # Start the main event loop
    root.mainloop()


if __name__ == "__main__":
    main()
