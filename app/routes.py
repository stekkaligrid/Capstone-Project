from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import UserCreate,UserResponse,TokenResponse,LoginRequest
from passlib.context import CryptContext
from app.models import User
from app.db import sessionLocal
from app.auth import verify_password,create_access_token,hash_password,pwd_context

router = APIRouter()


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

@router.post("/login", response_model=TokenResponse)
def login(user : LoginRequest, db : Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    if not verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    new_token = create_access_token(
        data={"sub":db_user.email}
    )

    return {
        "access_type" : new_token,
        "token_type" : "bearer"
    }