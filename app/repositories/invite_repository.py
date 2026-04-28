from app.models import Invitation, BoardMember


class InviteRepository:
    def __init__(self, db):
        self.db = db

    def create_invite(self, invite):
        self.db.add(invite)
        self.db.commit()
        self.db.refresh(invite)
        return invite

    def get_by_token(self, token: str):
        return self.db.query(Invitation).filter(Invitation.token == token).first()

    def get_member(self, board_id: int, user_id: int):
        return (
            self.db.query(BoardMember)
            .filter(BoardMember.board_id == board_id, BoardMember.user_id == user_id)
            .first()
        )

    def add_member(self, member):
        self.db.add(member)
        self.db.commit()

    def commit(self):
        self.db.commit()
