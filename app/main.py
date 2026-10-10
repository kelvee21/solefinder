import sqlite3

from fastapi import Depends, FastAPI, HTTPException

from app.db import schemas
from app.database import get_db, init_db

init_db()
app = FastAPI(title="SoleFinder")


@app.post("/merchants", status_code=201, response_model=schemas.MerchantOut)
def register_merchant(data: schemas.MerchantIn, db: sqlite3.Connection = Depends(get_db)):
    cur = db.execute(
        "INSERT INTO merchants (name, email) VALUES (?, ?)",
        (data.name, data.email),
    )
    db.commit()
    row = db.execute("SELECT id, name, email FROM merchants WHERE id = ?",
                     (cur.lastrowid,)).fetchone()
    return dict(row)


@app.post("/shoes", status_code=201, response_model=schemas.ShoeOut)
def add_shoe(data: schemas.ShoeIn, db: sqlite3.Connection = Depends(get_db)):
    cur = db.execute(
        "INSERT INTO shoes (brand, model, price) VALUES (?, ?, ?)",
        (data.brand, data.model, data.price),
    )
    db.commit()
    row = db.execute("SELECT id, brand, model, price FROM shoes WHERE id = ?",
                     (cur.lastrowid,)).fetchone()
    return dict(row)


@app.get("/shoes", response_model=list[schemas.ShoeOut])
def list_shoes(db: sqlite3.Connection = Depends(get_db)):
    rows = db.execute("SELECT id, brand, model, price FROM shoes ORDER BY id").fetchall()
    return [dict(r) for r in rows]