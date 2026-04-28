from app.models import Board
from app.repositories.board_repository import BoardRepository
from fastapi import HTTPException


class BoardService:
    def __init__(self, repo: BoardRepository):
        self.repo = repo

    def create_board(self, payload, current_user):
        board = Board(
            name=payload.name, description=payload.description, owner_id=current_user.id
        )

        return self.repo.create(board)

    def get_my_boards(self, current_user):
        return self.repo.get_by_owner(current_user.id)
