# models/user_model.py
from database.db_config import get_connection


def get_user(username, password, role=None):
    """
    Returns user row (id, username, password, role, student_id)
    matching username + password (+ optional role).
    """
    conn = get_connection()
    cur = conn.cursor()

    if role:
        cur.execute("""
            SELECT id, username, password, role, student_id
            FROM users
            WHERE username = ? AND password = ? AND role = ?
        """, (username, password, role))
    else:
        cur.execute("""
            SELECT id, username, password, role, student_id
            FROM users
            WHERE username = ? AND password = ?
        """, (username, password))

    row = cur.fetchone()
    conn.close()
    return row


def create_student_user(username, password, student_id):
    """
    Create a login user for a student (role = 'student').
    username can be same as roll number.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO users (username, password, role, student_id)
        VALUES (?, ?, 'student', ?)
    """, (username, password, student_id))
    conn.commit()
    conn.close()
