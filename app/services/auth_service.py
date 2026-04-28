from app.models import User
from app.auth import hash_password, verify_password, create_access_token
from app.repositories.user_repository import UserRepository
from fastapi import HTTPException


class AuthService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register(self, payload):
        existing = self.repo.get_by_email(payload.email)

        if existing:
            raise HTTPException(status_code=400, detail="Email already registered")

        user = User(
            email=payload.email,
            password_hash=hash_password(payload.password),
            first_name=payload.first_name,
            last_name=payload.last_name,
        )

        return self.repo.create(user)

    def login(self, email: str, password: str):
        user = self.repo.get_by_email(email)

        if not user or not verify_password(password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        token = create_access_token({"sub": user.email})

        return {"access_token": token, "token_type": "bearer"}
