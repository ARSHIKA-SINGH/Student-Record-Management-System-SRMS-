# gui/view_tickets_student.py
import tkinter as tk
from tkinter import ttk
from utils.constants import *
from models import ticket_model


class ViewTicketsStudentWindow(tk.Toplevel):
    def __init__(self, master, student_id):
        super().__init__(master)
        self.student_id = student_id

        self.title("My Tickets")
        self.geometry("700x400")
        self.configure(bg=BG_COLOR)

        tk.Label(self, text="My Tickets", font=FONT_TITLE, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)

        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=26)
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

        columns = ("id", "title", "status", "created_at")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col.title())
            self.tree.column(col, width=150)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.load_data()

    def load_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        rows = ticket_model.get_tickets_by_student(self.student_id)
        for r in rows:
            # r: id, title, description, status, created_at
            self.tree.insert("", "end", values=(r[0], r[1], r[3], r[4]))
