import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class Task:
    def __init__(self, description, category, date, time, important):
        self.description = description
        self.category = category
        self.date = date
        self.time = time
        self.important = important
        self.completed = tk.BooleanVar(value=False)


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Stylish To-Do List ✨")
        self.root.geometry("700x500")
        self.root.configure(bg="#f4f4f4")
        self.tasks = []

        # ===== Modern Theme =====
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TFrame", background="#f4f4f4")
        style.configure("TLabel", background="#f4f4f4", font=("Segoe UI", 10))
        style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=5)
        style.configure("Important.TLabel", foreground="red", font=("Segoe UI", 10, "bold"))
        style.configure("Done.TCheckbutton", font=("Segoe UI", 10, "overstrike"), foreground="gray")

        # ===== Main Container =====
        main_frame = ttk.Frame(root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # ===== Scrollable Task Area =====
        self.task_canvas = tk.Canvas(main_frame, bg="white", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.task_canvas.yview)
        self.task_container = ttk.Frame(self.task_canvas)

        self.task_container.bind(
            "<Configure>",
            lambda e: self.task_canvas.configure(scrollregion=self.task_canvas.bbox("all"))
        )

        self.task_canvas.create_window((0, 0), window=self.task_container, anchor="nw")
        self.task_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.task_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # ===== Column Headers =====
        header_frame = ttk.Frame(root, padding=5)
        header_frame.pack(fill=tk.X)
        headers = ["Task", "Category", "Date", "Time", "Priority"]
        for i, col in enumerate(headers):
            ttk.Label(header_frame, text=col, font=("Segoe UI", 11, "bold")).grid(row=0, column=i, padx=10)

        # ===== Form to Add Tasks =====
        form_frame = ttk.Frame(root, padding=10, relief=tk.RIDGE)
        form_frame.pack(fill=tk.X, padx=10, pady=10)

        ttk.Label(form_frame, text="Description:").grid(row=0, column=0, sticky=tk.W)
        self.desc_entry = ttk.Entry(form_frame, width=40)
        self.desc_entry.grid(row=0, column=1, pady=2, sticky=tk.W)

        ttk.Label(form_frame, text="Category:").grid(row=1, column=0, sticky=tk.W)
        self.category_var = tk.StringVar()
        categories = ['Work', 'Home', 'Fun', 'Others']
        self.category_combo = ttk.Combobox(form_frame, values=categories, textvariable=self.category_var, state="readonly")
        self.category_combo.grid(row=1, column=1, pady=2, sticky=tk.W)
        self.category_combo.current(0)

        ttk.Label(form_frame, text="Date (YYYY-MM-DD):").grid(row=2, column=0, sticky=tk.W)
        self.date_entry = ttk.Entry(form_frame)
        self.date_entry.grid(row=2, column=1, pady=2, sticky=tk.W)

        ttk.Label(form_frame, text="Time (HH:MM):").grid(row=3, column=0, sticky=tk.W)
        self.time_entry = ttk.Entry(form_frame)
        self.time_entry.grid(row=3, column=1, pady=2, sticky=tk.W)

        self.important_var = tk.BooleanVar()
        self.imp_check = ttk.Checkbutton(form_frame, text="Important", variable=self.important_var)
        self.imp_check.grid(row=4, column=1, sticky=tk.W)

        self.add_button = ttk.Button(form_frame, text="➕ Add Task", command=self.add_task)
        self.add_button.grid(row=5, column=0, columnspan=2, pady=5, sticky="ew")

        # ===== Action Buttons =====
        action_frame = ttk.Frame(root, padding=10)
        action_frame.pack(fill=tk.X, padx=10, pady=5)

        self.mark_done_btn = ttk.Button(action_frame, text="✅ Mark Selected Done", command=self.mark_done)
        self.mark_done_btn.pack(side=tk.LEFT, padx=5)

        self.delete_btn = ttk.Button(action_frame, text="🗑 Delete Selected", command=self.delete_selected)
        self.delete_btn.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        desc = self.desc_entry.get().strip()
        cat = self.category_var.get()
        date = self.date_entry.get().strip()
        time = self.time_entry.get().strip()
        important = self.important_var.get()

        if not desc:
            messagebox.showwarning("Input error", "Description cannot be empty.")
            return
        if date:
            try:
                datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                messagebox.showwarning("Input error", "Date must be YYYY-MM-DD format.")
                return
        if time:
            try:
                datetime.strptime(time, "%H:%M")
            except ValueError:
                messagebox.showwarning("Input error", "Time must be HH:MM format.")
                return

        new_task = Task(desc, cat, date, time, important)
        self.tasks.append(new_task)
        self.render_tasks()

        self.desc_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.important_var.set(False)

    def render_tasks(self):
        for widget in self.task_container.winfo_children():
            widget.destroy()

        for i, task in enumerate(self.tasks):
            bg_color = "#f9f9f9" if i % 2 == 0 else "#ffffff"
            row = ttk.Frame(self.task_container, style="TFrame")
            row.grid(row=i, column=0, sticky="ew")
            row.configure(style="TFrame")
            row.grid_columnconfigure(0, weight=1)

            cb_style = "Done.TCheckbutton" if task.completed.get() else "TCheckbutton"
            cb = ttk.Checkbutton(row, text=task.description, variable=task.completed, style=cb_style)
            cb.grid(row=0, column=0, sticky=tk.W, padx=(5, 5))

            ttk.Label(row, text=task.category).grid(row=0, column=1, padx=10)
            ttk.Label(row, text=task.date).grid(row=0, column=2, padx=10)
            ttk.Label(row, text=task.time).grid(row=0, column=3, padx=10)

            if task.important:
                ttk.Label(row, text="Important", style="Important.TLabel").grid(row=0, column=4, padx=10)
            else:
                ttk.Label(row, text="").grid(row=0, column=4, padx=10)

    def mark_done(self):
        self.render_tasks()

    def delete_selected(self):
        self.tasks = [t for t in self.tasks if not t.completed.get()]
        self.render_tasks()


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
