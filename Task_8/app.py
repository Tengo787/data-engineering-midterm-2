from fastapi import FastAPI
import sqlite3

app = FastAPI()

def get_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, age FROM users")
    users = [{"id": row[0], "name": row[1], "age": row[2]} for row in cursor.fetchall()]
    conn.close()
    return users

@app.get("/users")
def read_users():
    return get_users()
