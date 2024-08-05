import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("500x400")

        self.contacts = []

        # Labels and Entry Fields
        tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Phone").grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Email").grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        # Buttons
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=3, column=0, pady=10)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=3, column=1)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=3, column=2)

        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=4, column=0, columnspan=3, pady=10)

        # Listbox and Scrollbar
        self.contact_listbox = tk.Listbox(root, width=50, height=10)
        self.contact_listbox.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
        self.contact_listbox.bind("<<ListboxSelect>>", self.load_contact)

        self.scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=self.contact_listbox.yview)
        self.scrollbar.grid(row=5, column=3, sticky='ns')
        self.contact_listbox.config(yscrollcommand=self.scrollbar.set)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name and phone:
            self.contacts.append({"name": name, "phone": phone, "email": email})
            self.contact_listbox.insert(tk.END, name)
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name and Phone are required.")

    def update_contact(self):
        try:
            selected_index = self.contact_listbox.curselection()[0]
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()

            if name and phone:
                self.contacts[selected_index] = {"name": name, "phone": phone, "email": email}
                self.contact_listbox.delete(selected_index)
                self.contact_listbox.insert(selected_index, name)
                self.clear_entries()
            else:
                messagebox.showwarning("Warning", "Name and Phone are required.")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a contact to update.")

    def delete_contact(self):
        try:
            selected_index = self.contact_listbox.curselection()[0]
            del self.contacts[selected_index]
            self.contact_listbox.delete(selected_index)
            self.clear_entries()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a contact to delete.")

    def search_contact(self):
        search_name = self.name_entry.get().lower()
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contacts:
            if search_name in contact["name"].lower():
                self.contact_listbox.insert(tk.END, contact["name"])

    def load_contact(self, event):
        try:
            selected_index = self.contact_listbox.curselection()[0]
            contact = self.contacts[selected_index]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(tk.END, contact["name"])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(tk.END, contact["phone"])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(tk.END, contact["email"])
        except IndexError:
            pass

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
