import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

def generate_password():
    try:
        length = int(length_var.get())
        if length < 4:
            result_var.set("At least 4 characters needed.")
            return
        chars = ""
        if use_letters.get():
            chars += string.ascii_letters
        if use_digits.get():
            chars += string.digits
        if use_symbols.get():
            chars += string.punctuation
        if not chars:
            result_var.set("Select at least one character set.")
            return
        password = ''.join(random.choice(chars) for _ in range(length))
        result_var.set(password)
    except ValueError:
        result_var.set("Enter a valid number.")

def copy_password():
    pwd = result_var.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

def toggle_password():
    if show_pwd.get():
        output_entry.config(show="")
    else:
        output_entry.config(show="*")

# --- GUI Setup ---
root = tk.Tk()
root.title("✨ Attractive Password Generator")
root.geometry("400x340")
root.config(bg="#f1f2f6")

# Style
style = ttk.Style(root)
style.theme_use('clam')
style.configure("TButton", padding=6, relief="flat", background="#5352ed", foreground="white", font=('Arial', 10, 'bold'))
style.configure("TLabel", background="#f1f2f6", font=("Arial", 11))
style.configure("Header.TLabel", font=("Arial", 18, "bold"), foreground="#3742fa", background="#f1f2f6")

length_var = tk.StringVar(value="12")
result_var = tk.StringVar()
use_letters = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=True)
show_pwd = tk.BooleanVar(value=False)

# Layout
header = ttk.Label(root, text="Password Generator", style="Header.TLabel")
header.pack(pady=(16,10))

frame = tk.Frame(root, bg="#f1f2f6")
frame.pack(pady=10)

ttk.Label(frame, text="Length:").grid(row=0, column=0, sticky="w", padx=6, pady=6)
length_spin = ttk.Spinbox(frame, from_=4, to=64, textvariable=length_var, width=8)
length_spin.grid(row=0, column=1, padx=6, pady=6)

ttk.Label(frame, text="Include:").grid(row=1, column=0, sticky="w", padx=6, pady=6)
tk.Checkbutton(frame, text="Letters", variable=use_letters, bg="#f1f2f6", font=("Arial", 10)).grid(row=1, column=1, sticky="w")
tk.Checkbutton(frame, text="Digits", variable=use_digits, bg="#f1f2f6", font=("Arial", 10)).grid(row=2, column=1, sticky="w")
tk.Checkbutton(frame, text="Symbols", variable=use_symbols, bg="#f1f2f6", font=("Arial", 10)).grid(row=3, column=1, sticky="w")

generate_btn = ttk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=(8, 8))

ttk.Label(root, text="Generated Password:").pack(pady=(6,2))
output_entry = ttk.Entry(root, textvariable=result_var, font=("Consolas", 13), width=26)
output_entry.pack(pady=(0,4))
output_entry.config(show="*")

show_checkbox = tk.Checkbutton(root, text='Show Password', variable=show_pwd, command=toggle_password, bg="#f1f2f6")
show_checkbox.pack()

copy_btn = ttk.Button(root, text="Copy to Clipboard", command=copy_password)
copy_btn.pack(pady=(8, 6))

root.mainloop()
