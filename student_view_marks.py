# gui/student_view_marks.py
import tkinter as tk
from tkinter import ttk
from utils.constants import *
from models import marks_model


class StudentViewMarksWindow(tk.Toplevel):
    def __init__(self, master, student_id):
        super().__init__(master)
        self.student_id = student_id

        self.title("My Marks")
        self.geometry("800x400")
        self.configure(bg=BG_COLOR)

        tk.Label(
            self,
            text="My Marks",
            font=FONT_TITLE,
            bg=BG_COLOR,
            fg=TEXT_COLOR
        ).pack(pady=10)

        # Style for table
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=26)
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

        columns = (
            "exam_name",
            "subject1",
            "subject2",
            "subject3",
            "subject4",
            "subject5",
            "total",
            "percentage",
            "grade",
        )

        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.heading("exam_name", text="Exam")
        self.tree.heading("subject1", text="Sub 1")
        self.tree.heading("subject2", text="Sub 2")
        self.tree.heading("subject3", text="Sub 3")
        self.tree.heading("subject4", text="Sub 4")
        self.tree.heading("subject5", text="Sub 5")
        self.tree.heading("total", text="Total")
        self.tree.heading("percentage", text="%")
        self.tree.heading("grade", text="Grade")

        for col in columns:
            self.tree.column(col, width=80)

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        self.load_data()

    def load_data(self):
        # Clear existing
        for row in self.tree.get_children():
            self.tree.delete(row)

        rows = marks_model.get_marks_by_student(self.student_id)
        # rows: exam_name, s1, s2, s3, s4, s5, total, percentage, grade
        for r in rows:
            self.tree.insert("", "end", values=r)
