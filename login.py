# gui/login.py
import tkinter as tk
from tkinter import ttk
from utils.constants import *
from utils.helpers import show_error
from gui.dashboard import Dashboard
from gui.student_dashboard import StudentDashboard
from models import user_model


class LoginWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=BG_COLOR)
        self.pack(fill="both", expand=True)

        master.title(APP_TITLE + " - Login")

        # ✅ Center Card (NO FIXED HEIGHT)
        container = tk.Frame(self, bg=CARD_COLOR)
        container.place(relx=0.5, rely=0.5, anchor="center", width=360)

        tk.Label(
            container, text="Welcome 👋",
            font=FONT_TITLE, bg=CARD_COLOR, fg=TEXT_COLOR
        ).pack(pady=(15, 5))

        tk.Label(
            container, text="Login Portal",
            font=FONT_SUBTITLE, bg=CARD_COLOR, fg=PRIMARY_COLOR
        ).pack(pady=(0, 15))

        self.role = tk.StringVar(value="Admin")
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # ---------- ROLE ----------
        tk.Label(container, text="Login As", bg=CARD_COLOR, fg=TEXT_COLOR, font=FONT_LABEL).pack(anchor="w", padx=25)
        ttk.Combobox(
            container,
            textvariable=self.role,
            values=["Admin", "Student"],
            state="readonly"
        ).pack(padx=25, pady=(5, 10), fill="x")

        # ---------- USERNAME ----------
        tk.Label(container, text="Username", bg=CARD_COLOR, fg=TEXT_COLOR, font=FONT_LABEL).pack(anchor="w", padx=25)
        tk.Entry(container, textvariable=self.username, font=FONT_LABEL).pack(
            padx=25, pady=(5, 10), fill="x"
        )

        # ---------- PASSWORD ----------
        tk.Label(container, text="Password", bg=CARD_COLOR, fg=TEXT_COLOR, font=FONT_LABEL).pack(anchor="w", padx=25)
        tk.Entry(container, textvariable=self.password, show="*", font=FONT_LABEL).pack(
            padx=25, pady=(5, 20), fill="x"
        )

        # ✅ LOGIN BUTTON (NOW VISIBLE)
        tk.Button(
            container,
            text="Login",
            bg=PRIMARY_COLOR,
            fg="white",
            font=FONT_BUTTON,
            relief="flat",
            height=2,
            cursor="hand2",
            command=self.login
        ).pack(padx=25, pady=(0, 20), fill="x")

        tk.Label(
            container,
            text="Admin: admin / admin123",
            bg=CARD_COLOR,
            fg="#6b7280",
            font=("Segoe UI", 9)
        ).pack(pady=(0, 15))

    def login(self):
        u = self.username.get().strip()
        p = self.password.get().strip()
        role = self.role.get().lower()

        user = user_model.get_user(u, p, role)
        if not user:
            show_error("Invalid username, password, or role")
            return

        for w in self.master.winfo_children():
            w.destroy()

        if role == "admin":
            self.master.geometry("1000x600")
            Dashboard(self.master)
        else:
            student_id = user[4]
            self.master.geometry("900x550")
            StudentDashboard(self.master, student_id, u)
