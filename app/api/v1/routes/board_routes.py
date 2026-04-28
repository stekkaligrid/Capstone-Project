from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas import BoardCreate, BoardResponse
from app.services.board_service import BoardService
from app.repositories.board_repository import BoardRepository
from app.dependencies.auth import get_current_user

router = APIRouter(tags=["Boards"])


def get_board_service(db: Session = Depends(get_db)):
    repo = BoardRepository(db)
    return BoardService(repo)


@router.post("/boards", response_model=BoardResponse)
def create_board(
    payload: BoardCreate,
    current_user=Depends(get_current_user),
    service: BoardService = Depends(get_board_service),
):
    return service.create_board(payload, current_user)


@router.get("/boards", response_model=list[BoardResponse])
def get_boards(
    current_user=Depends(get_current_user),
    service: BoardService = Depends(get_board_service),
):
    return service.get_my_boards(current_user)
