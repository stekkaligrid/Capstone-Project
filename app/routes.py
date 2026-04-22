from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import UserCreate,UserResponse
from passlib.context import CryptContext
from app.models import User
from app.db import sessionLocal

router = APIRouter()

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password : str):
    return pwd_context.hash(password)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserResponse)
def register(user : UserCreate, db : Session = Depends(get_db)):

    reg_user = db.query(User).filter(User.email == user.email).first()

    if reg_user:
        raise HTTPException(status_code=409, detail="Email already Registered")
    
    new_user = User(
        email = user.email,
        password_hash = hash_password(user.password),
        first_name = user.first_name,
        last_name = user.last_name
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user