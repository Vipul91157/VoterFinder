import sqlite3
from pathlib import Path
from config import DATABASE_PATH


def create_database():

    # Ensure the data folder exists
    Path(DATABASE_PATH).parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DATABASE_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS voters (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        ac_no TEXT,

        part_no TEXT,

        serial_no TEXT,

        house_no TEXT,

        section_no TEXT,

        name TEXT,

        relation_type TEXT,

        relation_name TEXT,

        epic_no TEXT,

        gender TEXT,

        age TEXT,

        UNIQUE(ac_no, part_no, serial_no)

    )
    """)

    conn.commit()

    conn.close()

    print("Database Ready")