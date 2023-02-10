import tkinter as tk

class ToDoList:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")

        self.tasks = []

        self.task_label = tk.Label(master, text="Task:")
        self.task_label.grid(row=0, column=0, sticky="W")

        self.task_entry = tk.Entry(master)
        self.task_entry.grid(row=0, column=1)

        self.add_task_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=2)

        self.tasks_list = tk.Listbox(master)
        self.tasks_list.grid(row=1, column=0, columnspan=3)

        self.remove_task_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_task_button.grid(row=2, column=0, columnspan=3)

    def add_task(self):
        task = self.task_entry.get()
        self.tasks.append(task)
        self.tasks_list.insert("end", task)
        self.task_entry.delete(0, "end")

    def remove_task(self):
        selected_task = self.tasks_list.get("active")
        if selected_task:
            self.tasks.remove(selected_task)
            self.tasks_list.delete("active")

root = tk.Tk()
app = ToDoList(root)
root.mainloop()
