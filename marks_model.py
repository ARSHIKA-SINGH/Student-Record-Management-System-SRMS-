from database.db_config import get_connection


def save_marks(student_id, exam_name, s1, s2, s3, s4, s5):
    s1 = int(s1)
    s2 = int(s2)
    s3 = int(s3)
    s4 = int(s4)
    s5 = int(s5)
    total = s1 + s2 + s3 + s4 + s5
    percentage = total / 5.0

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    conn = get_connection()
    cur = conn.cursor()

    # Check if already marks for this student & exam
    cur.execute("""
        SELECT id FROM marks WHERE student_id = ? AND exam_name = ?
    """, (student_id, exam_name))
    row = cur.fetchone()

    if row:
        # Update
        cur.execute("""
            UPDATE marks
            SET subject1=?, subject2=?, subject3=?, subject4=?, subject5=?, total=?, percentage=?, grade=?
            WHERE id=?
        """, (s1, s2, s3, s4, s5, total, percentage, grade, row[0]))
    else:
        # Insert
        cur.execute("""
            INSERT INTO marks (student_id, exam_name, subject1, subject2, subject3, subject4, subject5, total, percentage, grade)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (student_id, exam_name, s1, s2, s3, s4, s5, total, percentage, grade))

    conn.commit()
    conn.close()

    return total, percentage, grade


def get_marks_by_student(student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT exam_name, subject1, subject2, subject3, subject4, subject5, total, percentage, grade
        FROM marks
        WHERE student_id = ?
    """, (student_id,))
    rows = cur.fetchall()
    conn.close()
    return rows


def get_all_results():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT s.roll, s.name, m.exam_name, m.total, m.percentage, m.grade
        FROM marks m
        JOIN students s ON s.id = m.student_id
        ORDER BY m.percentage DESC
    """)
    rows = cur.fetchall()
    conn.close()
    return rows
