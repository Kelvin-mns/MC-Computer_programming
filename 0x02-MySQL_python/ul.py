import tkinter as tk
from tkinter import messagebox
from functools import partial

# import the CRUD functions
from contacts_manager import create_contact, get_all_contacts, updata_contacts, delete_contacts

#Create the main aplication window
window = tk. tk()
window.title("Address Book")

#Create labels and entry fields
label_name = tk.Label(window, text="Name:")
entry_name = tk.Entry(window)

label_email = tk.Label(window, text="Email:")
entry_email = tk.Entry(window)

label_phone = tk.Label(window, text="Phone")
entry_phone = tk.Entry(window)

contact_listbox = tk.listbox(window, width=50)

def load_contacts():
    contact_listbox.delete(0, tk.END)
    contacts = get_all_contacts()
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact.name} - {contact.email} - {contact.phone}")

# function to add a new contact
def add_contact():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    create_contact(name, email, phone)
    load_contacts()
    messagebox.shoinfo("Success," "contact added successfully.")

#function to update a contact
def update_selected_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        contact_id = selected_index[0] + 1
        name = entry_name.get()
        email = entry_email.get()
        phone = entry_phone.get()
        updata_contacts(contact_id, name, email, phone)
        load_contacts()
        messagebox.showinfo("Success", "contact updated successfuly.")
    else:
        messagebox.showerror("Error",  "No contact selected.")
#function to delet a contact
def delete_selected_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        contact_id = selected_index[0] + 1
        delete_contacts(contact_id) 
        load_contacts()
        messagebox.showinfo("Success", "contact deleted successfully.")
    else:
        messagebox.showerror("Error", "No contact selected.")

# set the layout of the UI elements
label_name.pack()
entry_name.pack()

label_email.pack()
entry_email.pack()

label_phone.pack()
entry_phone.pack()

contact_listbox.pack()

button_add = tk.Button(window, text="Add contact", command=add_contact)
button_update = tk.Button(window, text="Update contact", commend=update_selected_contact)
button_delete = tk.Button(window, text="Delete contact", command=delete_selected_contact)

button_add.pack()
button_update.pack()
button_delete.pack()

# load contacts on application startup
load_contacts()

# start the main event loop
window.mainloop()


