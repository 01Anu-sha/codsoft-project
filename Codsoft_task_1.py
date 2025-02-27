import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    """Add a new task to the list."""
    task_name = task_entry.get().strip()
    if task_name:
        tasks.append({"task": task_name, "completed": False})
        save_tasks(tasks)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def update_task_list():
    """Update the listbox with tasks."""
    task_listbox.delete(0, tk.END)
    for index, task in enumerate(tasks):
        status = "✔" if task["completed"] else "❌"
        task_listbox.insert(tk.END, f"{index + 1}. {task['task']} [{status}]")

def mark_task_completed():
    """Mark the selected task as completed."""
    try:
        selected_index = task_listbox.curselection()[0]
        tasks[selected_index]["completed"] = True
        save_tasks(tasks)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

def delete_task():
    """Delete the selected task."""
    try:
        selected_index = task_listbox.curselection()[0]
        del tasks[selected_index]
        save_tasks(tasks)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Load existing tasks
tasks = load_tasks()

# Create main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")
root.configure(bg="#E3F2FD")  # Light blue background

# Title Label
title_label = tk.Label(root, text="To-Do List", font=("Arial", 16, "bold"), bg="#E3F2FD", fg="#0D47A1")
title_label.pack(pady=5)

# Task Entry
task_entry = tk.Entry(root, width=20, bg="white", fg="black", font=("Arial", 13))
task_entry.pack(pady=5)

# Buttons with Colors
add_button = tk.Button(root, text="Add Task", command=add_task, bg="#4CAF50", fg="white", font=("Arial", 12))
add_button.pack(pady=2)

mark_button = tk.Button(root, text="Mark Completed", command=mark_task_completed, bg="#1976D2", fg="white", font=("Arial", 12))
mark_button.pack(pady=2)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="#D32F2F", fg="white", font=("Arial", 12))
delete_button.pack(pady=2)

# Task List with Color
task_listbox = tk.Listbox(root, width=50, height=12, bg="#FFDDC1", fg="black", font=("Arial", 12))
task_listbox.pack(pady=10)

# Load tasks into the listbox
update_task_list()

# Run the GUI
root.mainloop()
