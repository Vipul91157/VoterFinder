import sqlite3
from config import DATABASE_PATH

def search_by_name(name):
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM voters
        WHERE name LIKE ?
        ORDER BY name
    """, (f"%{name}%",))

    results = cursor.fetchall()

    conn.close()

    return results


def search_by_epic(epic_no):
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM voters
        WHERE epic_no = ?
    """, (epic_no.upper(),))

    results = cursor.fetchall()

    conn.close()

    return results