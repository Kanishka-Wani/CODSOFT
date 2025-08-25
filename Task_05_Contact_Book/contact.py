import tkinter as tk
from tkinter import ttk, messagebox

# Contact Book Data: List of dicts
contacts = []

def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    address = text_address.get("1.0", "end").strip()
    
    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone are required.")
        return
    
    # Check if contact with same phone exists -> update
    for c in contacts:
        if c['phone'] == phone:
            messagebox.showerror("Duplicate", "Contact with this phone number already exists.")
            return
    
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    update_contact_list()
    clear_fields()

def update_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Select Contact", "Select a contact to update.")
        return
    
    index = selected[0]
    contact = contacts[index]
    
    new_name = entry_name.get().strip()
    new_phone = entry_phone.get().strip()
    new_email = entry_email.get().strip()
    new_address = text_address.get("1.0", "end").strip()
    
    if not new_name or not new_phone:
        messagebox.showwarning("Input Error", "Name and Phone are required.")
        return
    
    # Check if new phone duplicates another contact
    for i, c in enumerate(contacts):
        if i != index and c['phone'] == new_phone:
            messagebox.showerror("Duplicate", "Another contact with this phone number exists.")
            return
    
    contacts[index] = {"name": new_name, "phone": new_phone, "email": new_email, "address": new_address}
    update_contact_list()
    clear_fields()

def delete_contact():
    selected = contact_list.curselection()
    if not selected:
        messagebox.showwarning("Select Contact", "Select a contact to delete.")
        return
    
    index = selected[0]
    confirm = messagebox.askyesno("Confirm Delete", f"Delete contact '{contacts[index]['name']}'?")
    if confirm:
        contacts.pop(index)
        update_contact_list()
        clear_fields()

def search_contacts():
    query = entry_search.get().strip().lower()
    contact_list.delete(0, tk.END)
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def on_contact_select(event):
    if not contact_list.curselection():
        return
    index = contact_list.curselection()[0]
    contact = contacts[index]
    entry_name.delete(0, tk.END)
    entry_name.insert(0, contact['name'])
    entry_phone.delete(0, tk.END)
    entry_phone.insert(0, contact['phone'])
    entry_email.delete(0, tk.END)
    entry_email.insert(0, contact['email'])
    text_address.delete("1.0", tk.END)
    text_address.insert(tk.END, contact['address'])

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    text_address.delete("1.0", tk.END)
    entry_search.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("600x500")
root.resizable(False, False)

# Frames for layout
frame_left = ttk.Frame(root, padding=10)
frame_left.pack(side=tk.LEFT, fill=tk.Y)

frame_right = ttk.Frame(root, padding=10)
frame_right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Left frame: Contact Form
ttk.Label(frame_left, text="Name *").pack(anchor=tk.W)
entry_name = ttk.Entry(frame_left, width=30)
entry_name.pack(anchor=tk.W, pady=2)

ttk.Label(frame_left, text="Phone *").pack(anchor=tk.W)
entry_phone = ttk.Entry(frame_left, width=30)
entry_phone.pack(anchor=tk.W, pady=2)

ttk.Label(frame_left, text="Email").pack(anchor=tk.W)
entry_email = ttk.Entry(frame_left, width=30)
entry_email.pack(anchor=tk.W, pady=2)

ttk.Label(frame_left, text="Address").pack(anchor=tk.W)
text_address = tk.Text(frame_left, width=30, height=5)
text_address.pack(anchor=tk.W, pady=2)

# Buttons
btn_add = ttk.Button(frame_left, text="Add Contact", command=add_contact)
btn_add.pack(fill=tk.X, pady=5)

btn_update = ttk.Button(frame_left, text="Update Contact", command=update_contact)
btn_update.pack(fill=tk.X, pady=5)

btn_delete = ttk.Button(frame_left, text="Delete Contact", command=delete_contact)
btn_delete.pack(fill=tk.X, pady=5)

btn_clear = ttk.Button(frame_left, text="Clear Fields", command=clear_fields)
btn_clear.pack(fill=tk.X, pady=5)

# Right frame: Contact list and search
ttk.Label(frame_right, text="Search (Name or Phone)").pack(anchor=tk.W)
entry_search = ttk.Entry(frame_right, width=40)
entry_search.pack(anchor=tk.W, pady=2)
entry_search.bind("<KeyRelease>", lambda e: search_contacts())

contact_list = tk.Listbox(frame_right, height=20, width=40)
contact_list.pack(pady=5, fill=tk.BOTH, expand=True)
contact_list.bind("<<ListboxSelect>>", on_contact_select)

# Initialize empty list
update_contact_list()

root.mainloop()
