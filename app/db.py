import sqlite3


def get_user(user_id):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # Parameterized query — SQL injection fixed
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()
