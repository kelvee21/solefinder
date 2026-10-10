import sqlite3
from pathlib import Path

DB_URI = "file:solefinder?mode=memory&cache=shared"
SCHEMA = (Path(__file__).parent / "schema.sql").read_text()

# Keeps the in-memory DB alive for as long as the app runs.
_keepalive = sqlite3.connect(DB_URI, uri=True, check_same_thread=False)


def init_db():
    _keepalive.executescript(SCHEMA)
    _keepalive.commit()


def reset_db():
    """Used by tests to get a clean database."""
    _keepalive.executescript(
        "DROP TABLE IF EXISTS shoes;"
        "DROP TABLE IF EXISTS customers;"
        "DROP TABLE IF EXISTS merchants;"
    )
    init_db()


def get_db():
    conn = sqlite3.connect(DB_URI, uri=True, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        yield conn
    finally:
        conn.close()