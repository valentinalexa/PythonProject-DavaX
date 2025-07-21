import sqlite3
from datetime import datetime

DB_FILE = "math_operations.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()

        # Log table: all operations are saved here
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS operations_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                operation TEXT NOT NULL,
                input_1 REAL NOT NULL,
                input_2 REAL,
                result REAL NOT NULL,
                timestamp TEXT NOT NULL
            )
        """)

        # Cache table: one entry per operation + input_1 + input_2
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS operations_cache (
                operation TEXT NOT NULL,
                input_1 REAL NOT NULL,
                input_2 REAL,
                result REAL NOT NULL,
                PRIMARY KEY (operation, input_1, input_2)
            )
        """)

        conn.commit()

# -- Log Function --

def save_to_log(operation: str, input_1: float, input_2: float | None, result: float | int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO operations_log (operation, input_1, input_2, result, timestamp)
            VALUES (?, ?, ?, ?, ?)
        """, (operation, input_1, input_2, result, datetime.utcnow().isoformat()))
        conn.commit()

# -- Cache Functions --

def get_from_cache(operation: str, input_1: float, input_2: float | None):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT result FROM operations_cache
            WHERE operation = ? AND input_1 = ? AND input_2 IS ?
        """, (operation, input_1, input_2))
        row = cursor.fetchone()
        return row[0] if row else None

def save_to_cache(operation: str, input_1: float, input_2: float | None, result: float | int):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO operations_cache (operation, input_1, input_2, result)
            VALUES (?, ?, ?, ?)
        """, (operation, input_1, input_2, result))
        conn.commit()
 