# models/ticket_model.py
from database.db_config import get_connection
from datetime import datetime


def create_ticket(student_id, title, description):
    conn = get_connection()
    cur = conn.cursor()

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "Open"

    cur.execute("""
        INSERT INTO tickets (student_id, title, description, status, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (student_id, title, description, status, created_at))

    conn.commit()
    conn.close()


def get_tickets_by_student(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, title, description, status, created_at
        FROM tickets
        WHERE student_id = ?
        ORDER BY created_at DESC
    """, (student_id,))
    rows = cur.fetchall()
    conn.close()
    return rows


def get_all_tickets():
    """
    For admin: see all tickets with student info.
    """
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT t.id, s.roll, s.name, t.title, t.description, t.status, t.created_at
        FROM tickets t
        JOIN students s ON s.id = t.student_id
        ORDER BY t.created_at DESC
    """)
    rows = cur.fetchall()
    conn.close()
    return rows


def update_ticket_status(ticket_id, new_status):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE tickets
        SET status = ?
        WHERE id = ?
    """, (new_status, ticket_id))
    conn.commit()
    conn.close()
