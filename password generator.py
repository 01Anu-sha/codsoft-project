import random
import string
import tkinter as tk
from tkinter import messagebox


def generate_password():
    """Generate a password based on selected options."""
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4.")
            return

        characters = ""
        if uppercase_var.get():
            characters += string.ascii_uppercase
        if lowercase_var.get():
            characters += string.ascii_lowercase
        if numbers_var.get():
            characters += string.digits
        if special_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showwarning("Warning", "Please select at least one character type!")
            return

        password = ''.join(random.choice(characters) for _ in range(length))

        password_var.set(password)  # Display password in entry box
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")


def save_password():
    """Save password to a file."""
    password = password_var.get()
    if password:
        with open("saved_passwords.txt", "a") as file:
            file.write(password + "\n")
        messagebox.showinfo("Saved", "Password saved successfully!")
    else:
        messagebox.showwarning("Warning", "No password to save!")


# Create GUI window
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x400")
root.configure(bg="#E3F2FD")

# Title Label
title_label = tk.Label(root, text="Secure Password Generator", font=("Arial", 14, "bold"), bg="#E3F2FD", fg="#0D47A1")
title_label.pack(pady=10)

# Password Length Input
tk.Label(root, text="Enter password length:", font=("Arial", 12), bg="#E3F2FD").pack()
length_entry = tk.Entry(root, width=10, font=("Arial", 12))
length_entry.pack(pady=5)

# Character Options
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var, font=("Arial", 12),
                                    bg="#E3F2FD")
uppercase_checkbox.pack()

lowercase_checkbox = tk.Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var, font=("Arial", 12),
                                    bg="#E3F2FD")
lowercase_checkbox.pack()

numbers_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var, font=("Arial", 12), bg="#E3F2FD")
numbers_checkbox.pack()

special_checkbox = tk.Checkbutton(root, text="Include Special Characters", variable=special_var, font=("Arial", 12),
                                  bg="#E3F2FD")
special_checkbox.pack()
# Generate Button (Light Green)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#90EE90", fg="black",
                            font=("Arial", 12))
generate_button.pack(pady=5)

# Display Password
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 14), width=25, state="readonly",
                          justify="center")
password_entry.pack(pady=5)

# Save Button (Light Pink)
save_button = tk.Button(root, text="Save Password", command=save_password, bg="#FFB6C1", fg="black", font=("Arial", 12))
save_button.pack(pady=5)

# Run the GUI
root.mainloop()
