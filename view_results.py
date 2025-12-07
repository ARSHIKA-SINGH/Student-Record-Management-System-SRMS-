import tkinter as tk
from tkinter import ttk
from models import marks_model


class ViewResultsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("View Results")
        self.geometry("700x400")

        ttk.Label(self, text="Results", font=("Arial", 16, "bold")).pack(pady=10)

        self.tree = ttk.Treeview(
            self,
            columns=("roll", "name", "exam", "total", "percentage", "grade"),
            show="headings"
        )
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.title())
            self.tree.column(col, width=100)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.load_data()

    def load_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        rows = marks_model.get_all_results()
        for r in rows:
            self.tree.insert("", "end", values=r)
