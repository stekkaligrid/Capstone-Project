from app.models import Section
from app.repositories.section_repository import SectionRepository
from fastapi import HTTPException


class SectionService:
    def __init__(self, repo, board_repo):
        self.repo = repo
        self.board_repo = board_repo

    def create_section(self, board_id, payload, current_user):
        board = self.board_repo.get_by_id(board_id)

        if not board:
            raise HTTPException(status_code=404, detail="Board not found")

        if board.owner_id != current_user.id:
            raise HTTPException(
                status_code=403, detail="Only owner can create sections"
            )

        section = Section(
            name=payload.name, description=payload.description, board_id=board_id
        )

        return self.repo.create(section)

    def get_sections(self, board_id, current_user):
        board = self.board_repo.get_by_id(board_id)

        if not board:
            raise HTTPException(status_code=404, detail="Board not found")

        if board.owner_id != current_user.id:
            raise HTTPException(status_code=403, detail="Access denied")

        return self.repo.get_by_board(board_id)
