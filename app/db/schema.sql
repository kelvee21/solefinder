CREATE TABLE IF NOT EXISTS merchants (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name  TEXT NOT NULL CHECK (length(trim(name)) > 0),
    email TEXT NOT NULL UNIQUE
);
CREATE TABLE IF NOT EXISTS shoes (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT NOT NULL CHECK (length(trim(brand)) > 0),
    model TEXT NOT NULL CHECK (length(trim(model)) > 0),
    price REAL NOT NULL CHECK (price > 0)
);