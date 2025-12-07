# database/db_config.py
import sqlite3

DB_NAME = "srms.db"


def get_connection():
    """
    Returns a new SQLite database connection.
    timeout added to avoid 'database is locked' errors.
    """
    return sqlite3.connect(DB_NAME, timeout=5)


def init_db():
    """
    Create all required tables if they do not exist
    and ensure default admin user is present.
    """
    conn = get_connection()
    cur = conn.cursor()

    # ---------------- STUDENTS ----------------
    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            class TEXT,
            branch TEXT,
            phone TEXT,
            email TEXT,
            address TEXT
        )
    """)

    # ---------------- MARKS ----------------
    cur.execute("""
        CREATE TABLE IF NOT EXISTS marks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            exam_name TEXT,
            subject1 INTEGER,
            subject2 INTEGER,
            subject3 INTEGER,
            subject4 INTEGER,
            subject5 INTEGER,
            total INTEGER,
            percentage REAL,
            grade TEXT,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    """)

    # ---------------- ATTENDANCE ----------------
    cur.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            date TEXT,
            status TEXT,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    """)

    # ---------------- USERS (LOGIN) ----------------
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL,             -- 'admin' or 'student'
            student_id INTEGER,             -- NULL for admin
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    """)

    # ---------------- TICKETS ----------------
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            status TEXT DEFAULT 'Open',     -- Open / In Progress / Closed
            created_at TEXT,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    """)

    # ---------------- DEFAULT ADMIN ----------------
    cur.execute("SELECT id FROM users WHERE role = 'admin'")
    admin_exists = cur.fetchone()

    if not admin_exists:
        cur.execute("""
            INSERT INTO users (username, password, role, student_id)
            VALUES ('admin', 'admin123', 'admin', NULL)
        """)

    conn.commit()
    conn.close()
