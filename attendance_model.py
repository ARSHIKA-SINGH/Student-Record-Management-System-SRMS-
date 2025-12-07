from database.db_config import get_connection


def mark_attendance(student_id, date_str, status):
    conn = get_connection()
    cur = conn.cursor()

    # Check if already marked for that day
    cur.execute("""
        SELECT id FROM attendance WHERE student_id = ? AND date = ?
    """, (student_id, date_str))
    row = cur.fetchone()

    if row:
        cur.execute("""
            UPDATE attendance
            SET status = ?
            WHERE id = ?
        """, (status, row[0]))
    else:
        cur.execute("""
            INSERT INTO attendance (student_id, date, status)
            VALUES (?, ?, ?)
        """, (student_id, date_str, status))

    conn.commit()
    conn.close()


def get_attendance_by_student(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT date, status
        FROM attendance
        WHERE student_id = ?
        ORDER BY date
    """, (student_id,))
    rows = cur.fetchall()
    conn.close()
    return rows


def get_attendance_summary(student_id):
    rows = get_attendance_by_student(student_id)
    total = len(rows)
    present = sum(1 for _, status in rows if status.lower() == "present")
    percentage = (present / total * 100) if total > 0 else 0
    return total, present, percentage
