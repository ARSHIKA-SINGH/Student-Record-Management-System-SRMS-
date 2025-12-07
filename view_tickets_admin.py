# gui/view_tickets_admin.py
import tkinter as tk
from tkinter import ttk
from utils.constants import *
from utils.helpers import show_info
from models import ticket_model


class ViewTicketsAdminWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("All Tickets")
        self.geometry("900x450")
        self.configure(bg=BG_COLOR)

        tk.Label(self, text="All Tickets", font=FONT_TITLE, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)

        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=26)
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

        columns = ("id", "roll", "name", "title", "status", "created_at")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col.title())
            self.tree.column(col, width=130)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        btn_frame = tk.Frame(self, bg=BG_COLOR)
        btn_frame.pack(pady=5)

        tk.Button(
            btn_frame,
            text="Mark In Progress",
            bg=PRIMARY_COLOR,
            fg="white",
            font=FONT_BUTTON,
            relief="flat",
            command=lambda: self.change_status("In Progress")
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            btn_frame,
            text="Mark Closed",
            bg="#16a34a",
            fg="white",
            font=FONT_BUTTON,
            relief="flat",
            command=lambda: self.change_status("Closed")
        ).grid(row=0, column=1, padx=5)

        self.load_data()

    def load_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        rows = ticket_model.get_all_tickets()
        for r in rows:
            # r: id, roll, name, title, desc, status, created_at
            self.tree.insert("", "end", values=(r[0], r[1], r[2], r[3], r[5], r[6]))

    def change_status(self, new_status):
        selected = self.tree.selection()
        if not selected:
            show_info("Select a ticket first.")
            return
        item = self.tree.item(selected[0])
        ticket_id = item["values"][0]
        ticket_model.update_ticket_status(ticket_id, new_status)
        self.load_data()
