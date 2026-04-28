from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas import SectionCreate, SectionResponse

from app.repositories.section_repository import SectionRepository
from app.repositories.board_repository import BoardRepository
from app.dependencies.auth import get_current_user
from app.services.section_service import SectionService

from app.dependencies.auth import get_current_user

router = APIRouter(tags=["Sections"])


def get_section_service(db: Session = Depends(get_db)):
    section_repo = SectionRepository(db)
    board_repo = BoardRepository(db)

    return SectionService(section_repo, board_repo)


@router.post("/boards/{board_id}/sections", response_model=SectionResponse)
def create_section(
    board_id: int,
    payload: SectionCreate,
    current_user=Depends(get_current_user),
    service: SectionService = Depends(get_section_service),
):
    return service.create_section(board_id, payload, current_user)


@router.get("/boards/{board_id}/sections", response_model=list[SectionResponse])
def get_sections(
    board_id: int,
    current_user=Depends(get_current_user),
    service: SectionService = Depends(get_section_service),
):
    return service.get_sections(board_id, current_user)
