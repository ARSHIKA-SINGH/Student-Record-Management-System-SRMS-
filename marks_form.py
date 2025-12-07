import tkinter as tk
from tkinter import ttk
from utils.helpers import show_info, show_error
from utils.validators import is_empty, is_valid_marks
from models import student_model, marks_model


class MarksFormWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Enter Marks")
        self.geometry("450x450")

        self.exam_var = tk.StringVar()
        self.roll_var = tk.StringVar()
        self.s1_var = tk.StringVar()
        self.s2_var = tk.StringVar()
        self.s3_var = tk.StringVar()
        self.s4_var = tk.StringVar()
        self.s5_var = tk.StringVar()

        ttk.Label(self, text="Marks Entry", font=("Arial", 16, "bold")).pack(pady=10)

        form = ttk.Frame(self)
        form.pack(pady=5, padx=10, fill="x")

        def add_row(label, var, row):
            ttk.Label(form, text=label).grid(row=row, column=0, sticky="w", pady=4)
            ttk.Entry(form, textvariable=var, width=25).grid(row=row, column=1, pady=4)

        add_row("Exam Name:", self.exam_var, 0)
        add_row("Roll No:", self.roll_var, 1)
        add_row("Subject 1:", self.s1_var, 2)
        add_row("Subject 2:", self.s2_var, 3)
        add_row("Subject 3:", self.s3_var, 4)
        add_row("Subject 4:", self.s4_var, 5)
        add_row("Subject 5:", self.s5_var, 6)

        ttk.Button(self, text="Save Marks", command=self.save_marks).pack(pady=10)

        self.result_lbl = ttk.Label(self, text="")
        self.result_lbl.pack(pady=5)

    def save_marks(self):
        exam = self.exam_var.get()
        roll = self.roll_var.get()
        s1 = self.s1_var.get()
        s2 = self.s2_var.get()
        s3 = self.s3_var.get()
        s4 = self.s4_var.get()
        s5 = self.s5_var.get()

        if is_empty(exam, roll, s1, s2, s3, s4, s5):
            show_error("All fields are required.")
            return

        if not is_valid_marks(s1, s2, s3, s4, s5):
            show_error("Marks must be numbers between 0 and 100.")
            return

        student = student_model.get_student_by_roll(roll)
        if not student:
            show_error("No student found with this roll.")
            return

        student_id = student[0]
        try:
            total, perc, grade = marks_model.save_marks(student_id, exam, s1, s2, s3, s4, s5)
            self.result_lbl.config(text=f"Total: {total} | %: {perc:.2f} | Grade: {grade}")
            show_info("Marks saved successfully.")
        except Exception as e:
            show_error(f"Error: {e}")
