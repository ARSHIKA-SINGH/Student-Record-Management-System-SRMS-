# gui/student_view_attendance.py
import tkinter as tk
from tkinter import ttk
from utils.constants import *
from models import attendance_model


class StudentViewAttendanceWindow(tk.Toplevel):
    def __init__(self, master, student_id):
        super().__init__(master)
        self.student_id = student_id

        self.title("My Attendance")
        self.geometry("700x450")
        self.configure(bg=BG_COLOR)

        tk.Label(
            self,
            text="My Attendance",
            font=FONT_TITLE,
            bg=BG_COLOR,
            fg=TEXT_COLOR
        ).pack(pady=10)

        # Summary label
        self.summary_lbl = tk.Label(
            self,
            text="",
            font=FONT_SUBTITLE,
            bg=BG_COLOR,
            fg=PRIMARY_COLOR
        )
        self.summary_lbl.pack(pady=5)

        # Style for table
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=26)
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

        columns = ("date", "status")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.heading("date", text="Date")
        self.tree.heading("status", text="Status")

        self.tree.column("date", width=150)
        self.tree.column("status", width=100)

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.load_data()

    def load_data(self):
        # Clear table
        for row in self.tree.get_children():
            self.tree.delete(row)

        rows = attendance_model.get_attendance_by_student(self.student_id)
        total, present, perc = attendance_model.get_attendance_summary(self.student_id)

        # Update summary text
        self.summary_lbl.config(
            text=f"Total Classes: {total}  |  Present: {present}  |  Attendance: {perc:.2f}%"
        )

        # Fill table
        for d, s in rows:
            self.tree.insert("", "end", values=(d, s))
