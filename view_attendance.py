import tkinter as tk
from tkinter import ttk
from models import student_model, attendance_model
from utils.helpers import show_info


class ViewAttendanceWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("View Attendance")
        self.geometry("700x450")

        self.roll_var = tk.StringVar()

        top = ttk.Frame(self)
        top.pack(pady=5, padx=10, fill="x")

        ttk.Label(top, text="Roll No:").pack(side="left")
        ttk.Entry(top, textvariable=self.roll_var, width=20).pack(side="left", padx=5)
        ttk.Button(top, text="Load", command=self.load_attendance).pack(side="left", padx=5)

        self.summary_lbl = ttk.Label(self, text="", font=("Arial", 11, "bold"))
        self.summary_lbl.pack(pady=5)

        self.tree = ttk.Treeview(self, columns=("date", "status"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.title())
            self.tree.column(col, width=150)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    def load_attendance(self):
        roll = self.roll_var.get().strip()
        if not roll:
            show_info("Enter roll number.")
            return
        student = student_model.get_student_by_roll(roll)
        if not student:
            show_info("No student found with this roll.")
            return

        student_id = student[0]
        rows = attendance_model.get_attendance_by_student(student_id)
        total, present, perc = attendance_model.get_attendance_summary(student_id)

        self.summary_lbl.config(
            text=f"Total: {total} | Present: {present} | Attendance %: {perc:.2f}"
        )

        for r in self.tree.get_children():
            self.tree.delete(r)
        for d, s in rows:
            self.tree.insert("", "end", values=(d, s))

