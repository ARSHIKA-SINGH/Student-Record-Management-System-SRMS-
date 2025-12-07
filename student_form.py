import tkinter as tk
from tkinter import ttk
from utils.helpers import show_info, show_error
from utils.validators import is_empty
from models import student_model


class StudentFormWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Student Form")
        self.geometry("400x450")
        self.resizable(False, False)

        self.student_id = None

        self.roll_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.class_var = tk.StringVar()
        self.branch_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()

        ttk.Label(self, text="Student Form", font=("Arial", 16, "bold")).pack(pady=10)

        form = ttk.Frame(self)
        form.pack(pady=5, padx=10, fill="x")

        def add_row(label, var, row):
            ttk.Label(form, text=label).grid(row=row, column=0, sticky="w", pady=4)
            ttk.Entry(form, textvariable=var, width=30).grid(row=row, column=1, pady=4)

        add_row("Roll No:", self.roll_var, 0)
        add_row("Name:", self.name_var, 1)
        add_row("Class:", self.class_var, 2)
        add_row("Branch:", self.branch_var, 3)
        add_row("Phone:", self.phone_var, 4)
        add_row("Email:", self.email_var, 5)

        ttk.Label(form, text="Address:").grid(row=6, column=0, sticky="nw", pady=4)
        self.address_text = tk.Text(form, width=23, height=4)
        self.address_text.grid(row=6, column=1, pady=4)

        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Save", command=self.save_student).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Clear", command=self.clear_form).grid(row=0, column=1, padx=5)

    def save_student(self):
        roll = self.roll_var.get()
        name = self.name_var.get()
        sclass = self.class_var.get()
        branch = self.branch_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_text.get("1.0", "end").strip()

        if is_empty(roll, name):
            show_error("Roll and Name are required.")
            return

        try:
            if self.student_id:  # update
                student_model.update_student(self.student_id, roll, name, sclass, branch, phone, email, address)
                show_info("Student updated successfully.")
            else:  # add new
                student_model.add_student(roll, name, sclass, branch, phone, email, address)
                show_info("Student added successfully.")
            self.clear_form()
        except Exception as e:
            show_error(f"Error saving student: {e}")

    def clear_form(self):
        self.student_id = None
        self.roll_var.set("")
        self.name_var.set("")
        self.class_var.set("")
        self.branch_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.address_text.delete("1.0", "end")
