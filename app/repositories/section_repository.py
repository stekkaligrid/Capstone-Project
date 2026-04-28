from app.models import Section


class SectionRepository:
    def __init__(self, db):
        self.db = db

    def create(self, section):
        self.db.add(section)
        self.db.commit()
        self.db.refresh(section)
        return section

    def get_by_board(self, board_id: int):
        return self.db.query(Section).filter(Section.board_id == board_id).all()

    def get_by_id(self, section_id: int):
        return self.db.query(Section).filter(Section.id == section_id).first()

    def delete(self, section):
        self.db.delete(section)
        self.db.commit()
