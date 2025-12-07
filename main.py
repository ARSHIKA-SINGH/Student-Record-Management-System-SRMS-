# main.py
import tkinter as tk
from database.db_config import init_db
from gui.login import LoginWindow

def main():
    init_db()

    root = tk.Tk()
    root.geometry("450x420")   # ✅ INCREASED HEIGHT
    root.title("Student Record Management System")

    LoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
