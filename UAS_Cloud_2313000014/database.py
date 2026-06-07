import sqlite3

DB_NAME = "laptop.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS laptop (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT,
        harga REAL,
        ram REAL,
        ssd REAL,
        processor REAL,
        merek REAL
    )
    """)

    conn.commit()
    conn.close()

def tambah_laptop(nama, harga, ram, ssd, processor, merek):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO laptop
    (nama, harga, ram, ssd, processor, merek)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (nama, harga, ram, ssd, processor, merek))

    conn.commit()
    conn.close()

def get_all_laptop():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM laptop")
    data = cur.fetchall()

    conn.close()
    return data

def hapus_laptop(id_laptop):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM laptop WHERE id=?",
        (id_laptop,)
    )

    conn.commit()
    conn.close()