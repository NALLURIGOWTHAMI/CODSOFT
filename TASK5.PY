import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Contact Book")

        # Create widgets
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_entry = tk.Entry(self.root)
        self.phone_label = tk.Label(self.root, text="Phone:")
        self.phone_entry = tk.Entry(self.root)
        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.contacts_listbox = tk.Listbox(self.root)

        # Layout widgets
        self.name_label.pack()
        self.name_entry.pack()
        self.phone_label.pack()
        self.phone_entry.pack()
        self.add_button.pack()
        self.contacts_listbox.pack()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        self.contacts_listbox.insert(tk.END, f"{name}: {phone}")
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.run()
