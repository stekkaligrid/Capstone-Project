from app.services.ticket_service import TicketService

class FakeTicket:
    def __init__(self,name,description,section_id,board_id,created_by):
        self.name = name
        self.description = description
        self.section_id = section_id
        self.board_id = board_id
        self.created_by = created_by
    
class FakeUser:
    def __init__(self,id):
        self.id = id

class Payload:
    def __init__(self):
        self.name = "Test Ticket"
        self.description = "Test Description"
        self.assigned_to = "Current user"

class FakeRepo:
    def __init__(self):
        self.tickets = []

    def create(self,ticket):
        self.tickets.append(ticket)
        return ticket
    
    def get_tickets(self):
        return self.tickets
    
class FakeSection:
    def __init__(self,id,board_id):
        self.id = id
        self.board_id = board_id

class FakeBoard:
    def __init__(self,id,owner_id):
        self.id = id
        self.owner_id = owner_id

class FakeSectionRepo:
    def get_by_id(self,section_id):
        return FakeSection(section_id,board_id=1)
    
class FakeBoardRepo:
    def get_by_id(self,board_id):
        return FakeBoard(board_id,owner_id=1)
    
def test_create_ticket():
    ticket_repo = FakeRepo()
    section_repo = FakeSectionRepo()
    board_repo = FakeBoardRepo()

    service = TicketService(ticket_repo,section_repo=section_repo,board_repo=board_repo)

    user = FakeUser(1)
    payload = Payload()

    result = service.create_ticket(section_id=1,payload=payload,current_user=user)

    assert result.name == "Test Ticket"
    assert result.section_id == 1
    assert result.board_id == 1 
    assert result.created_by == 1


