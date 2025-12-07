import tkinter as tk
from tkinter import ttk
from datetime import date
from models import student_model, attendance_model
from utils.helpers import show_info, show_error


class AttendanceFormWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Mark Attendance")
        self.geometry("500x400")

        self.date_var = tk.StringVar(value=str(date.today()))
        self.status_var = tk.StringVar(value="Present")

        ttk.Label(self, text="Mark Attendance", font=("Arial", 16, "bold")).pack(pady=10)

        top = ttk.Frame(self)
        top.pack(pady=5, padx=10, fill="x")

        ttk.Label(top, text="Date (YYYY-MM-DD):").grid(row=0, column=0, sticky="w", pady=4)
        ttk.Entry(top, textvariable=self.date_var, width=20).grid(row=0, column=1, pady=4)

        ttk.Label(top, text="Status:").grid(row=1, column=0, sticky="w", pady=4)
        status_cb = ttk.Combobox(top, textvariable=self.status_var, values=["Present", "Absent", "Late"], width=18)
        status_cb.grid(row=1, column=1, pady=4)
        status_cb.current(0)

        # Students list
        self.tree = ttk.Treeview(self, columns=("id", "roll", "name"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.title())
            self.tree.column(col, width=150)
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=5)
        ttk.Button(btn_frame, text="Mark for Selected", command=self.mark_for_selected).pack(side="left", padx=5)

        self.load_students()

    def load_students(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        rows = student_model.get_all_students()
        for r in rows:
            # r: id, roll, name, class, ...
            self.tree.insert("", "end", values=(r[0], r[1], r[2]))

    def mark_for_selected(self):
        selected = self.tree.selection()
        if not selected:
            show_info("Please select a student.")
            return
        item = self.tree.item(selected[0])
        student_id = item["values"][0]
        date_str = self.date_var.get().strip()
        status = self.status_var.get()
        if not date_str:
            show_error("Date is required.")
            return
        try:
            attendance_model.mark_attendance(student_id, date_str, status)
            show_info("Attendance saved.")
        except Exception as e:
            show_error(f"Error: {e}")
