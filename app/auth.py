from fastapi import APIRouter, HTTPException
from app.security import hash_password, verify_password, create_token

router = APIRouter(prefix="/auth", tags=["Auth"])

fake_db = {}


@router.post("/register")
def register(username: str, password: str):
    if username in fake_db:
        raise HTTPException(400, "User exists")

    fake_db[username] = hash_password(password)
    return {"message": "registered"}


@router.post("/login")
def login(username: str, password: str):
    hashed = fake_db.get(username)

    if not hashed or not verify_password(password, hashed):
        raise HTTPException(401, "Invalid credentials")

    token = create_token({"sub": username})
    return {"access_token": token, "token_type": "bearer"}