# gui/dashboard.py
import tkinter as tk
from utils.constants import *
from gui.student_form import StudentFormWindow
from gui.view_students import ViewStudentsWindow
from gui.marks_form import MarksFormWindow
from gui.view_results import ViewResultsWindow
from gui.attendance_form import AttendanceFormWindow
from gui.view_attendance import ViewAttendanceWindow
from gui.view_tickets_admin import ViewTicketsAdminWindow


class Dashboard(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=BG_COLOR)
        self.master.title(APP_TITLE + " - Admin Dashboard")
        self.pack(fill="both", expand=True)

        # ================= TITLE =================
        title = tk.Label(
            self,
            text="Student Record Management System",
            font=FONT_TITLE,
            bg=BG_COLOR,
            fg=TEXT_COLOR
        )
        title.pack(pady=15)

        subtitle = tk.Label(
            self,
            text="Admin Dashboard",
            font=FONT_SUBTITLE,
            bg=BG_COLOR,
            fg=PRIMARY_COLOR
        )
        subtitle.pack(pady=(0, 20))

        # ================= CARD =================
        card = tk.Frame(self, bg=CARD_COLOR)
        card.pack(padx=40, pady=20)

        # ================= BUTTONS =================
        self.create_button(card, "👨‍🎓 Manage Students", self.open_students, 0, 0)
        self.create_button(card, "📋 View Students", self.view_students, 0, 1)

        self.create_button(card, "📝 Enter Marks", self.enter_marks, 1, 0)
        self.create_button(card, "🏆 View Results", self.view_results, 1, 1)

        self.create_button(card, "✅ Mark Attendance", self.mark_attendance, 2, 0)
        self.create_button(card, "📊 View Attendance", self.view_attendance, 2, 1)

        # ✅ NEW: TICKETS BUTTON
        self.create_button(card, "🎫 View Tickets", self.view_tickets, 3, 0)

        # ================= EXIT =================
        tk.Button(
            self,
            text="Logout",
            bg="#dc2626",
            fg="white",
            font=FONT_BUTTON,
            width=15,
            relief="flat",
            cursor="hand2",
            command=self.master.destroy
        ).pack(pady=20)

    # ================= BUTTON FACTORY =================
    def create_button(self, parent, text, command, row, col):
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            bg=PRIMARY_COLOR,
            fg="white",
            font=FONT_BUTTON,
            width=25,
            height=2,
            relief="flat",
            cursor="hand2"
        )
        btn.grid(row=row, column=col, padx=20, pady=15)

    # ================= ACTIONS =================
    def open_students(self):
        StudentFormWindow(self.master)

    def view_students(self):
        ViewStudentsWindow(self.master)

    def enter_marks(self):
        MarksFormWindow(self.master)

    def view_results(self):
        ViewResultsWindow(self.master)

    def mark_attendance(self):
        AttendanceFormWindow(self.master)

    def view_attendance(self):
        ViewAttendanceWindow(self.master)

    # ✅ NEW METHOD
    def view_tickets(self):
        ViewTicketsAdminWindow(self.master)
