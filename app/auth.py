from passlib.context import CryptContext
from database import get_db

pwd_context = CryptContext(schemes=["bcrypt"])

def register_user(username, password, role="USER"):
    db = get_db()
    hashed_password = pwd_context.hash(password)
    db.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
               (username, hashed_password, role))
    db.commit()

def authenticate_user(username, password):
    db = get_db()
    user = db.execute("SELECT * FROM users WHERE username=?", (username,)).fetchone()
    if user and pwd_context.verify(password, user["password"]):
        return user
    return None
