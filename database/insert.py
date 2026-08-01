import sqlite3
from config import DATABASE_PATH


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def insert_voters(conn, voters):

    cursor = conn.cursor()

    cursor.executemany("""
        INSERT OR IGNORE INTO voters (
            ac_no,
            part_no,
            serial_no,
            house_no,
            section_no,
            name,
            relation_type,
            relation_name,
            epic_no,
            gender,
            age
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, [

        (
            voter["ac_no"],
            voter["part_no"],
            voter["serial_no"],
            voter["house_no"],
            voter["section_no"],
            voter["name"],
            voter["relation_type"],
            voter["relation_name"],
            voter["epic_no"],
            voter["gender"],
            voter["age"]
        )

        for voter in voters

    ])