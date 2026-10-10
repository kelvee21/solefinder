CREATE TABLE IF NOT EXISTS merchants (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name  TEXT NOT NULL CHECK (length(trim(name)) > 0),
    email TEXT NOT NULL UNIQUE
);