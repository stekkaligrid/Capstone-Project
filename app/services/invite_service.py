import secrets
from fastapi import HTTPException
from app.models import Invitation, BoardMember


class InviteService:
    def __init__(self, repo, board_repo):
        self.repo = repo
        self.board_repo = board_repo

    def create_invite(self, board_id, current_user):
        board = self.board_repo.get_by_id(board_id)

        if not board:
            raise HTTPException(status_code=404, detail="Board not found")

        if board.owner_id != current_user.id:
            raise HTTPException(status_code=403, detail="Only owner can invite users")

        token = secrets.token_urlsafe(16)

        invite = Invitation(board_id=board_id, token=token, created_by=current_user.id)

        return self.repo.create_invite(invite)

    def accept_invite(self, token, current_user):
        invite = self.repo.get_by_token(token)

        if not invite:
            raise HTTPException(status_code=404, detail="Invitation not found")

        if invite.used:
            raise HTTPException(status_code=400, detail="Invitation already used")

        existing = self.repo.get_member(invite.board_id, current_user.id)

        if existing:
            raise HTTPException(status_code=400, detail="Already a member")

        member = BoardMember(
            board_id=invite.board_id, user_id=current_user.id, role="member"
        )

        self.repo.add_member(member)

        invite.used = True
        self.repo.commit()

        return {"message": "Joined board successfully"}
