from fastapi import HTTPException
from app.models import Ticket


class TicketService:
    def __init__(self, repo, section_repo, board_repo):
        self.repo = repo
        self.section_repo = section_repo
        self.board_repo = board_repo

    def create_ticket(self, section_id, payload, current_user):
        section = self.section_repo.get_by_id(section_id)

        if not section:
            raise HTTPException(status_code=404, detail="Section not found")

        board = self.board_repo.get_by_id(section.board_id)

        if board.owner_id != current_user.id:
            raise HTTPException(status_code=403, detail="Only owner can create tickets")

        ticket = Ticket(
            name=payload.name,
            description=payload.description,
            section_id=section.id,
            board_id=section.board_id,
            created_by=current_user.id,
            assigned_to=payload.assigned_to,
        )

        return self.repo.create(ticket)

    def get_tickets(self, section_id, current_user):
        section = self.section_repo.get_by_id(section_id)

        if not section:
            raise HTTPException(status_code=404, detail="Section not found")

        board = self.board_repo.get_by_id(section.board_id)

        if board.owner_id != current_user.id:
            raise HTTPException(status_code=403, detail="Access denied")

        return self.repo.get_by_section(section_id)
