import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.task_list = []

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=30)
        self.task_entry.grid(row=0, column=0, padx=5)

        self.add_task_btn = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_task_btn.grid(row=0, column=1)

        self.update_task_btn = tk.Button(self.frame, text="Update Task", command=self.update_task)
        self.update_task_btn.grid(row=0, column=2)

        self.delete_task_btn = tk.Button(self.frame, text="Delete Task", command=self.delete_task)
        self.delete_task_btn.grid(row=0, column=3)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=4, pady=10)

        self.task_listbox.bind("<<ListboxSelect>>", self.load_task)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            updated_task = self.task_entry.get()
            if updated_task:
                self.task_list[selected_task_index] = updated_task
                self.task_listbox.delete(selected_task_index)
                self.task_listbox.insert(selected_task_index, updated_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a task.")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
            del self.task_list[selected_task_index]
            self.task_entry.delete(0, tk.END)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def load_task(self, event):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            selected_task = self.task_list[selected_task_index]
            self.task_entry.delete(0, tk.END)
            self.task_entry.insert(tk.END, selected_task)
        except IndexError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
