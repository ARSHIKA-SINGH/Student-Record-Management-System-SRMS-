import tkinter as tk
from tkinter import ttk
from models import student_model
from utils.helpers import show_info, show_error, ask_confirm


class ViewStudentsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("View Students")
        self.geometry("800x400")

        self.search_var = tk.StringVar()

        search_frame = ttk.Frame(self)
        search_frame.pack(fill="x", pady=5, padx=10)

        ttk.Label(search_frame, text="Search (Roll/Name):").pack(side="left")
        ttk.Entry(search_frame, textvariable=self.search_var, width=30).pack(side="left", padx=5)
        ttk.Button(search_frame, text="Search", command=self.search).pack(side="left", padx=5)
        ttk.Button(search_frame, text="Show All", command=self.load_data).pack(side="left", padx=5)

        self.tree = ttk.Treeview(self, columns=("id", "roll", "name", "class", "branch", "phone", "email"),
                                 show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.title())
            self.tree.column(col, width=100)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=5)
        ttk.Button(btn_frame, text="Delete Selected", command=self.delete_selected).pack(side="left", padx=5)

        self.load_data()

    def load_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        rows = student_model.get_all_students()
        for r in rows:
            self.tree.insert("", "end", values=r)

    def search(self):
        keyword = self.search_var.get().strip()
        rows = student_model.search_students(keyword) if keyword else student_model.get_all_students()
        for row in self.tree.get_children():
            self.tree.delete(row)
        for r in rows:
            self.tree.insert("", "end", values=r)

    def delete_selected(self):
        selected = self.tree.selection()
        if not selected:
            show_info("Please select a student.")
            return
        if not ask_confirm("Are you sure to delete this student?"):
            return
        item = self.tree.item(selected[0])
        student_id = item["values"][0]
        try:
            student_model.delete_student(student_id)
            show_info("Student deleted.")
            self.load_data()
        except Exception as e:
            show_error(f"Error deleting: {e}")
