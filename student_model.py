# models/student_model.py
from database.db_config import get_connection
from models.user_model import create_student_user


def add_student(roll, name, sclass, branch, phone, email, address):
    conn = get_connection()
    cur = conn.cursor()

    # Insert student
    cur.execute("""
        INSERT INTO students (roll, name, class, branch, phone, email, address)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (roll, name, sclass, branch, phone, email, address))

    student_id = cur.lastrowid  # get newly created student id

    # ✅ FIRST commit & close this connection (releases lock)
    conn.commit()
    conn.close()

    # ✅ THEN create student login using a NEW connection
    create_student_user(
        username=roll,              # roll number as username
        password="student123",      # default password
        student_id=student_id
    )


def update_student(student_id, roll, name, sclass, branch, phone, email, address):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE students
        SET roll = ?, name = ?, class = ?, branch = ?, phone = ?, email = ?, address = ?
        WHERE id = ?
    """, (roll, name, sclass, branch, phone, email, address, student_id))

    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = get_connection()
    cur = conn.cursor()

    # delete from students
    cur.execute("DELETE FROM students WHERE id = ?", (student_id,))
    # also delete related user login (if exists)
    cur.execute("DELETE FROM users WHERE student_id = ?", (student_id,))

    conn.commit()
    conn.close()


def get_all_students():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, roll, name, class, branch, phone, email FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows


def get_student_by_roll(roll):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE roll = ?", (roll,))
    row = cur.fetchone()
    conn.close()
    return row
