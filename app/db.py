import sqlite3


def get_user(user_id):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # SQL injection: user input formatted directly into the query (FIXED in C1)
    query = "SELECT * FROM users WHERE id = '%s'" % user_id
    cursor.execute(query)
    return cursor.fetchone()
