# gui/student_dashboard.py
import tkinter as tk
from utils.constants import *
from gui.ticket_form import TicketFormWindow
from gui.view_tickets_student import ViewTicketsStudentWindow
from gui.student_view_marks import StudentViewMarksWindow
from gui.student_view_attendance import StudentViewAttendanceWindow


class StudentDashboard(tk.Frame):
    def __init__(self, master, student_id, username):
        super().__init__(master, bg=BG_COLOR)
        self.master = master
        self.student_id = student_id
        self.username = username

        self.pack(fill="both", expand=True)

        master.title(f"{APP_TITLE} - Student Panel")

        # ===== Title =====
        title = tk.Label(
            self,
            text="Student Panel",
            font=FONT_TITLE,
            bg=BG_COLOR,
            fg=TEXT_COLOR
        )
        title.pack(pady=20)

        subtitle = tk.Label(
            self,
            text=f"Logged in as: {username}",
            font=FONT_SUBTITLE,
            bg=BG_COLOR,
            fg=PRIMARY_COLOR
        )
        subtitle.pack(pady=(0, 20))

        # ===== Card with buttons =====
        card = tk.Frame(self, bg=CARD_COLOR)
        card.pack(padx=40, pady=20)

        # Row 0
        tk.Button(
            card,
            text="📩 Raise New Ticket",
            bg=PRIMARY_COLOR,
            fg="white",
            font=FONT_BUTTON,
            width=25,
            height=2,
            relief="flat",
            cursor="hand2",
            command=self.open_ticket_form
        ).grid(row=0, column=0, padx=20, pady=15)

        tk.Button(
            card,
            text="📜 View My Tickets",
            bg=PRIMARY_COLOR,
            fg="white",
            font=FONT_BUTTON,
            width=25,
            height=2,
            relief="flat",
            cursor="hand2",
            command=self.view_my_tickets
        ).grid(row=0, column=1, padx=20, pady=15)

        # Row 1 – NEW FEATURES
        tk.Button(
            card,
            text="📝 View My Marks",
            bg=PRIMARY_COLOR,
            fg="white",
            font=FONT_BUTTON,
            width=25,
            height=2,
            relief="flat",
            cursor="hand2",
            command=self.view_my_marks
        ).grid(row=1, column=0, padx=20, pady=15)

        tk.Button(
            card,
            text="📊 View My Attendance",
            bg=PRIMARY_COLOR,
            fg="white",
            font=FONT_BUTTON,
            width=25,
            height=2,
            relief="flat",
            cursor="hand2",
            command=self.view_my_attendance
        ).grid(row=1, column=1, padx=20, pady=15)

        # ===== Logout =====
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

    # ---------- Actions ----------
    def open_ticket_form(self):
        TicketFormWindow(self.master, self.student_id)

    def view_my_tickets(self):
        ViewTicketsStudentWindow(self.master, self.student_id)

    def view_my_marks(self):
        StudentViewMarksWindow(self.master, self.student_id)

    def view_my_attendance(self):
        StudentViewAttendanceWindow(self.master, self.student_id)
