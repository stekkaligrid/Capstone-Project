from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas import TicketCreate, TicketResponse

from app.repositories.ticket_repository import TicketRepository
from app.repositories.section_repository import SectionRepository
from app.repositories.board_repository import BoardRepository

from app.services.ticket_service import TicketService

from app.dependencies.auth import get_current_user

router = APIRouter(tags=["Tickets"])


def get_ticket_service(db: Session = Depends(get_db)):
    ticket_repo = TicketRepository(db)
    section_repo = SectionRepository(db)
    board_repo = BoardRepository(db)

    return TicketService(ticket_repo, section_repo, board_repo)


@router.post("/sections/{section_id}/tickets", response_model=TicketResponse)
def create_ticket(
    section_id: int,
    payload: TicketCreate,
    current_user=Depends(get_current_user),
    service: TicketService = Depends(get_ticket_service),
):
    return service.create_ticket(section_id, payload, current_user)


@router.get("/sections/{section_id}/tickets", response_model=list[TicketResponse])
def get_tickets(
    section_id: int,
    current_user=Depends(get_current_user),
    service: TicketService = Depends(get_ticket_service),
):
    return service.get_tickets(section_id, current_user)
