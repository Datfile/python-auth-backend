from fastapi import FastAPI, HTTPException
from auth import register_user, authenticate_user
from models import create_tables

app = FastAPI()
create_tables()

@app.post("/register")
def register(data: dict):
    try:
        register_user(data["username"], data["password"])
        return {"message": "User registered successfully"}
    except:
        raise HTTPException(status_code=400, detail="User already exists")

@app.post("/login")
def login(data: dict):
    user = authenticate_user(data["username"], data["password"])
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "role": user["role"]}
