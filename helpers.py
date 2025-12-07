from tkinter import messagebox


def show_info(msg, title="Info"):
    messagebox.showinfo(title, msg)


def show_error(msg, title="Error"):
    messagebox.showerror(title, msg)


def ask_confirm(msg, title="Confirm"):
    return messagebox.askyesno(title, msg)
