import tkinter as tk
from tkinter import messagebox, simpledialog
import json

CONTACTS_FILE = "contacts.json"


def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_contacts():
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter Name:")
    phone = simpledialog.askstring("Add Contact", "Enter Phone Number:")
    email = simpledialog.askstring("Add Contact", "Enter Email:")
    address = simpledialog.askstring("Add Contact", "Enter Address:")

    if name and phone:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts()
        update_contact_list()
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required!")


def update_contact_list():
    contact_list.delete(0, tk.END)
    for idx, (name, details) in enumerate(contacts.items(), start=1):
        contact_list.insert(tk.END, f"{idx}. {name} - {details['Phone']}")


def search_contact():
    search_term = simpledialog.askstring("Search Contact", "Enter Name or Phone Number:")
    if not search_term:
        return

    for name, details in contacts.items():
        if search_term in name or search_term in details["Phone"]:
            messagebox.showinfo("Contact Found",
                                f"Name: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}")
            return

    messagebox.showerror("Not Found", "Contact not found!")


def update_contact():
    name = simpledialog.askstring("Update Contact", "Enter Name of Contact to Update:")
    if name in contacts:
        phone = simpledialog.askstring("Update Contact", "Enter New Phone Number:",
                                       initialvalue=contacts[name]["Phone"])
        email = simpledialog.askstring("Update Contact", "Enter New Email:", initialvalue=contacts[name]["Email"])
        address = simpledialog.askstring("Update Contact", "Enter New Address:", initialvalue=contacts[name]["Address"])

        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts()
        update_contact_list()
    else:
        messagebox.showerror("Not Found", "Contact not found!")


def delete_contact():
    name = simpledialog.askstring("Delete Contact", "Enter Name of Contact to Delete:")
    if name in contacts:
        if messagebox.askyesno("Delete", f"Are you sure you want to delete {name}?"):
            del contacts[name]
            save_contacts()
            update_contact_list()
    else:
        messagebox.showerror("Not Found", "Contact not found!")


# Load existing contacts
contacts = load_contacts()

# Create GUI
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x400")
root.configure(bg="light green")


def create_button(text, command):
    return tk.Button(root, text=text, command=command, bg="light blue", fg="black")


tk.Button(root, text="Add Contact", command=add_contact, bg="light blue", fg="black").pack(pady=5)
tk.Button(root, text="Search Contact", command=search_contact, bg="light blue", fg="black").pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact, bg="light blue", fg="black").pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact, bg="light blue", fg="black").pack(pady=5)

contact_list = tk.Listbox(root, width=50, height=10, bg="light yellow", fg="black")
contact_list.pack(pady=10)
update_contact_list()

root.mainloop()
