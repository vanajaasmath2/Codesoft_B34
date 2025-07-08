import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

contacts = []

# ---------------------- Functions ----------------------
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name and phone:
        contacts.append({
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        })
        messagebox.showinfo("Success", "Contact added!")
        clear_entries()
        show_contacts()
    else:
        messagebox.showerror("Error", "Name and Phone are required!")

def show_contacts():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    query = entry_search.get().lower()
    listbox.delete(0, tk.END)
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def delete_contact():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        contacts.pop(index)
        show_contacts()
        messagebox.showinfo("Deleted", "Contact deleted!")
    else:
        messagebox.showwarning("Warning", "Select a contact to delete.")

def update_contact():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]

        # Pop-up to get updated values
        name = simpledialog.askstring("Update", "Enter name:", initialvalue=contact['name'])
        phone = simpledialog.askstring("Update", "Enter phone:", initialvalue=contact['phone'])
        email = simpledialog.askstring("Update", "Enter email:", initialvalue=contact['email'])
        address = simpledialog.askstring("Update", "Enter address:", initialvalue=contact['address'])

        if name and phone:
            contacts[index] = {'name': name, 'phone': phone, 'email': email, 'address': address}
            show_contacts()
            messagebox.showinfo("Updated", "Contact updated!")
        else:
            messagebox.showerror("Error", "Name and Phone are required!")
    else:
        messagebox.showwarning("Warning", "Select a contact to update.")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# ---------------------- GUI Setup ----------------------
root = tk.Tk()
root.title("Contact Management System")

# Labels and Entries
tk.Label(root, text="Name").grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Phone").grid(row=1, column=0, padx=5, pady=5)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Email").grid(row=2, column=0, padx=5, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Address").grid(row=3, column=0, padx=5, pady=5)
entry_address = tk.Entry(root)
entry_address.grid(row=3, column=1, padx=5, pady=5)

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, columnspan=2, pady=5)

tk.Label(root, text="Search").grid(row=5, column=0, padx=5, pady=5)
entry_search = tk.Entry(root)
entry_search.grid(row=5, column=1, padx=5, pady=5)

tk.Button(root, text="Search", command=search_contact).grid(row=6, column=0, pady=5)
tk.Button(root, text="Show All", command=show_contacts).grid(row=6, column=1, pady=5)
tk.Button(root, text="Update", command=update_contact).grid(row=7, column=0, pady=5)
tk.Button(root, text="Delete", command=delete_contact).grid(row=7, column=1, pady=5)

# Contact Listbox
listbox = tk.Listbox(root, width=50)
listbox.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
