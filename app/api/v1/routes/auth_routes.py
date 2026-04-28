from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import LoginRequest


from app.db import get_db
from app.schemas import UserCreate, UserResponse, TokenResponse
from app.services.auth_service import AuthService
from app.repositories.user_repository import UserRepository

router = APIRouter(tags=["Auth"])


def get_auth_service(db: Session = Depends(get_db)):
    repo = UserRepository(db)
    return AuthService(repo)


@router.post("/register", response_model=UserResponse)
def register(payload: UserCreate, service: AuthService = Depends(get_auth_service)):
    return service.register(payload)


@router.post("/login", response_model=TokenResponse)
def login(
    payload: LoginRequest,
    service: AuthService = Depends(get_auth_service)
):
    return service.login(
        payload.email,
        payload.password
    )