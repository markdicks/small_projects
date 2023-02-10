import tkinter as tk
import os

class ToDoList:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")
        master.geometry("500x500")

        self.tasks = []
        self.filename = "tasks.txt"

        # Load tasks from file, if it exists
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.tasks = [line.strip() for line in f.readlines()]

        self.task_label = tk.Label(master, text="Task:")
        self.task_label.grid(row=0, column=0, sticky="W")

        self.task_entry = tk.Entry(master)
        self.task_entry.grid(row=0, column=1)
        self.task_entry.bind("<Return>", self.add_task)

        self.add_task_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=2)

        self.tasks_list = tk.Listbox(master)
        self.tasks_list.grid(row=1, column=0, columnspan=3)

        for task in self.tasks:
            self.tasks_list.insert("end", task)

        self.remove_task_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_task_button.grid(row=2, column=0, columnspan=3)
        self.error_label = tk.Label(master, text="", fg="red")
        self.error_label.grid(row=3, column=0, columnspan=3)

        # Use the weight property to adjust the layout to the aspect ratio of the display
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=3)
        self.master.columnconfigure(2, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=3)
        self.master.rowconfigure(2, weight=1)

    def add_task(self, event=None):
        task = self.task_entry.get()
        if len(task) < 3:
            self.error_label.config(text="Task must be at least 3 characters long.")
        else:
            self.tasks.append(task)
            self.tasks_list.insert("end", task)
            self.task_entry.delete(0, "end")
            with open(self.filename, "a") as f:
                f.write(task + "\n")
            self.error_label.config(text="")

    def remove_task(self):
        selected_task = self.tasks_list.get("active")
        if selected_task:
            self.tasks.remove(selected_task)
            self.tasks_list.delete("active")
            with open(self.filename, "w") as f:
                f.write("\n".join(self.tasks))

root = tk.Tk()
app = ToDoList(root)
root.mainloop()
