import tkinter as tk
from tkinter import messagebox, simpledialog, Listbox, ttk

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        self.root.geometry("400x450")
        self.contacts = []

        self.main_menu = tk.Menu(self.root)
        self.root.config(menu=self.main_menu)

        self.contact_menu = tk.Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Contacts", menu=self.contact_menu)
        self.contact_menu.add_command(label="Add Contact", command=self.add_contact)
        self.contact_menu.add_command(label="View Contacts", command=self.view_contacts)
        self.contact_menu.add_command(label="Search Contact", command=self.search_contact)
        self.contact_menu.add_separator()
        self.contact_menu.add_command(label="Exit", command=self.root.quit)

        self.welcome_label = tk.Label(self.root, text="Welcome to the Contact Management System", font=("Helvetica", 16, "bold"))
        self.welcome_label.pack(pady=20)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.add_button = ttk.Button(self.button_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=0, column=0, padx=10)

        self.view_button = ttk.Button(self.button_frame, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=0, column=1, padx=10)

        self.search_button = ttk.Button(self.button_frame, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=0, column=2, padx=10)

        self.recent_frame = tk.LabelFrame(self.root, text="Recently Added Contacts", font=("Helvetica", 14))
        self.recent_frame.pack(pady=10, padx=10, fill="both", expand="yes")

        self.recent_list = Listbox(self.recent_frame)
        self.recent_list.pack(fill=tk.BOTH, expand=True)

    def add_contact(self):
        contact_window = tk.Toplevel(self.root)
        contact_window.title("Add Contact")
        contact_window.geometry("300x200")

        tk.Label(contact_window, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        tk.Label(contact_window, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
        tk.Label(contact_window, text="Email:").grid(row=2, column=0, padx=10, pady=5)
        tk.Label(contact_window, text="Address:").grid(row=3, column=0, padx=10, pady=5)

        name_entry = ttk.Entry(contact_window)
        phone_entry = ttk.Entry(contact_window)
        email_entry = ttk.Entry(contact_window)
        address_entry = ttk.Entry(contact_window)

        name_entry.grid(row=0, column=1, padx=10, pady=5)
        phone_entry.grid(row=1, column=1, padx=10, pady=5)
        email_entry.grid(row=2, column=1, padx=10, pady=5)
        address_entry.grid(row=3, column=1, padx=10, pady=5)

        def save_contact():
            name = name_entry.get()
            phone = phone_entry.get()
            email = email_entry.get()
            address = address_entry.get()
            if name and phone and email and address:
                self.contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
                messagebox.showinfo("Success", "Contact added successfully!")
                contact_window.destroy()
                self.update_recent_contacts()
            else:
                messagebox.showwarning("Warning", "Please fill in all fields")

        save_button = ttk.Button(contact_window, text="Add", command=save_contact)
        save_button.grid(row=4, column=0, columnspan=2, pady=10)

    def view_contacts(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("Contact List")
        view_window.geometry("400x300")

        contact_listbox = Listbox(view_window, selectmode=tk.SINGLE)
        contact_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        for index, contact in enumerate(self.contacts):
            contact_str = f"{index + 1}. {contact['name']} - {contact['phone']}"
            contact_listbox.insert(tk.END, contact_str)

        def on_select(event):
            selected_index = contact_listbox.curselection()[0]
            selected_contact = self.contacts[selected_index]
            update_window = tk.Toplevel(self.root)
            update_window.title("Update/Delete Contact")
            update_window.geometry("300x200")

            tk.Label(update_window, text="Name:").grid(row=0, column=0, padx=10, pady=5)
            tk.Label(update_window, text="Phone:").grid(row=1, column=0, padx=10, pady=5)
            tk.Label(update_window, text="Email:").grid(row=2, column=0, padx=10, pady=5)
            tk.Label(update_window, text="Address:").grid(row=3, column=0, padx=10, pady=5)

            name_entry = ttk.Entry(update_window)
            phone_entry = ttk.Entry(update_window)
            email_entry = ttk.Entry(update_window)
            address_entry = ttk.Entry(update_window)

            name_entry.grid(row=0, column=1, padx=10, pady=5)
            phone_entry.grid(row=1, column=1, padx=10, pady=5)
            email_entry.grid(row=2, column=1, padx=10, pady=5)
            address_entry.grid(row=3, column=1, padx=10, pady=5)

            name_entry.insert(0, selected_contact['name'])
            phone_entry.insert(0, selected_contact['phone'])
            email_entry.insert(0, selected_contact['email'])
            address_entry.insert(0, selected_contact['address'])

            def update_contact():
                self.contacts[selected_index]['name'] = name_entry.get()
                self.contacts[selected_index]['phone'] = phone_entry.get()
                self.contacts[selected_index]['email'] = email_entry.get()
                self.contacts[selected_index]['address'] = address_entry.get()
                messagebox.showinfo("Success", "Contact updated successfully!")
                update_window.destroy()
                view_window.destroy()
                self.view_contacts()

            def delete_contact():
                self.contacts.pop(selected_index)
                messagebox.showinfo("Success", "Contact deleted successfully!")
                update_window.destroy()
                view_window.destroy()
                self.view_contacts()
                self.update_recent_contacts()

            update_button = ttk.Button(update_window, text="Update", command=update_contact)
            update_button.grid(row=4, column=0, padx=10, pady=10)

            delete_button = ttk.Button(update_window, text="Delete", command=delete_contact)
            delete_button.grid(row=4, column=1, padx=10, pady=10)

        contact_listbox.bind('<<ListboxSelect>>', on_select)

    def search_contact(self):
        search_term = simpledialog.askstring("Search", "Enter Name or Phone:")
        results = [contact for contact in self.contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
        if results:
            search_window = tk.Toplevel(self.root)
            search_window.title("Search Results")
            search_window.geometry("400x300")

            for contact in results:
                contact_str = f"{contact['name']} - {contact['phone']}"
                tk.Label(search_window, text=contact_str).pack(pady=5)
        else:
            messagebox.showinfo("No Results", "No contacts found.")

    def update_recent_contacts(self):
        self.recent_list.delete(0, tk.END)
        recent_contacts = self.contacts[-3:]
        for contact in recent_contacts:
            contact_str = f"{contact['name']} - {contact['phone']}"
            self.recent_list.insert(tk.END, contact_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
