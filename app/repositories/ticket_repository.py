from app.models import Ticket


class TicketRepository:
    def __init__(self, db):
        self.db = db

    def create(self, ticket):
        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)
        return ticket

    def get_by_section(self, section_id: int):
        return self.db.query(Ticket).filter(Ticket.section_id == section_id).all()

    def get_by_id(self, ticket_id: int):
        return self.db.query(Ticket).filter(Ticket.id == ticket_id).first()

    def delete(self, ticket):
        self.db.delete(ticket)
        self.db.commit()
