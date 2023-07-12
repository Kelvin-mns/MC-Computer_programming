from tkinter import Tk
from ui import addressBookUI, load_contact

# Entry point of the application
if__name__=="__main__":
# create the Tkinter root window
root = Tk()
root.title("Address Book")

# create an instance of the AddressBooKUI
address_book_ui = addressBookUI(root)

# start the tkinter event loop
root.mainloop()