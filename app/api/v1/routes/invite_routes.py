from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.dependencies.auth import get_current_user

from app.repositories.invite_repository import InviteRepository
from app.repositories.board_repository import BoardRepository

from app.services.invite_service import InviteService

router = APIRouter(tags=["Invitations"])


def get_invite_service(db: Session = Depends(get_db)):
    invite_repo = InviteRepository(db)
    board_repo = BoardRepository(db)

    return InviteService(invite_repo, board_repo)


@router.post("/boards/{board_id}/invite")
def create_invitation(
    board_id: int,
    current_user=Depends(get_current_user),
    service: InviteService = Depends(get_invite_service),
):
    return service.create_invite(board_id, current_user)


@router.post("/invitations/{token}/accept")
def accept_invitation(
    token: str,
    current_user=Depends(get_current_user),
    service: InviteService = Depends(get_invite_service),
):
    return service.accept_invite(token, current_user)
