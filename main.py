import tkinter as tk
from tkinter import messagebox


def add():
    text = textBox.get()
    if text:
        listBox.insert(tk.END, text)
        textBox.delete(0, tk.END)
    else:
        messagebox.showerror("Add Error!","You must add text in the text box before clicking Add!")


def remove():
    selected_task = listBox.curselection()
    if selected_task:
        listBox.delete(tk.ANCHOR)
    else:
        messagebox.showerror("Remove Error!", "You must select an item to remove before clicking Remove!")


def cross():
    selected_task = listBox.curselection()
    if selected_task:
        listBox.itemconfig(selected_task, fg='gray')
        listBox.selection_clear(selected_task)



root = tk.Tk()
root.title("To-Do List")
task = tk.StringVar()
textBox = tk.Entry(root, width=30, textvariable=task)
textBox.grid(row=0, column=0, padx=10, pady=10)

listBox = tk.Listbox(root, width=50, height=20)
listBox.grid(row=1, column=0, padx=10)

addButton = tk.Button(root, text="Add", command=add)
addButton.grid(row=0, column=1, padx=5)
removeButton = tk.Button(root, text="Remove", command=remove)
removeButton.grid(row=0, column=2, padx=5)
crossButton = tk.Button(root, text="Cross", command=cross)
crossButton.grid(row=0, column=3, padx=5)
root.geometry("600x400")
root.mainloop()
