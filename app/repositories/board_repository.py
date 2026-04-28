from app.models import Board


class BoardRepository:
    def __init__(self, db):
        self.db = db

    def create(self, board):
        self.db.add(board)
        self.db.commit()
        self.db.refresh(board)
        return board

    def get_by_id(self, board_id: int):
        return self.db.query(Board).filter(Board.id == board_id).first()

    def get_by_owner(self, user_id: int):
        return self.db.query(Board).filter(Board.owner_id == user_id).all()
