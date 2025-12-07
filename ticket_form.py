# gui/ticket_form.py
import tkinter as tk
from tkinter import ttk
from utils.constants import *
from utils.helpers import show_info, show_error
from models import ticket_model


class TicketFormWindow(tk.Toplevel):
    def __init__(self, master, student_id):
        super().__init__(master)
        self.student_id = student_id

        self.title("Raise Ticket")
        self.geometry("450x350")
        self.configure(bg=BG_COLOR)
        self.resizable(False, False)

        self.title_var = tk.StringVar()
        self.desc_text = None

        tk.Label(self, text="Raise Ticket", font=FONT_TITLE, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)

        card = tk.Frame(self, bg=CARD_COLOR)
        card.pack(padx=15, pady=10, fill="both", expand=True)

        tk.Label(card, text="Title", bg=CARD_COLOR, fg=TEXT_COLOR, font=FONT_LABEL).grid(
            row=0, column=0, sticky="w", padx=10, pady=(10, 3)
        )
        tk.Entry(card, textvariable=self.title_var, font=FONT_LABEL, width=35).grid(
            row=0, column=1, padx=10, pady=(10, 3)
        )

        tk.Label(card, text="Description", bg=CARD_COLOR, fg=TEXT_COLOR, font=FONT_LABEL).grid(
            row=1, column=0, sticky="nw", padx=10, pady=5
        )
        self.desc_text = tk.Text(card, width=35, height=7)
        self.desc_text.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(
            card,
            text="Submit Ticket",
            bg=PRIMARY_COLOR,
            fg="white",
            font=FONT_BUTTON,
            relief="flat",
            command=self.submit_ticket
        ).grid(row=2, column=0, columnspan=2, pady=15)

    def submit_ticket(self):
        title = self.title_var.get().strip()
        desc = self.desc_text.get("1.0", "end").strip()

        if not title or not desc:
            show_error("Both title and description are required.")
            return

        try:
            ticket_model.create_ticket(self.student_id, title, desc)
            show_info("Ticket submitted successfully.")
            self.destroy()
        except Exception as e:
            show_error(f"Error: {e}")
