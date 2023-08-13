import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        tasks.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task = listbox.curselection()
    if selected_task:
        tasks.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create a listbox to display tasks
tasks = tk.Listbox(root)
tasks.pack(padx=10, pady=10)

# Create an entry widget for adding tasks
entry = tk.Entry(root)
entry.pack(padx=10, pady=5)

# Create "Add" and "Remove" buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(padx=10, pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(padx=10, pady=5)

# Start the GUI event loop
root.mainloop()
