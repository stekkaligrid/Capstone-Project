from app.services.board_service import BoardService

class FakeUser:
    def __init__(self,id):
        self.id = id

class Payload:
    def __init__(self):
        self.name = "Test Board"
        self.description = "Test description"

class FakeBoard: 
    def __int__(self,id,name,owner_id):
        self.id = id
        self.name = name
        self.owner_id = owner_id

class FakeRepo:

    def __init__(self):
        self.boards = []

    def create(self,board):
        self.boards.append(board)
        return board

    def get_by_owner(self, owner_id):
        return self.boards
    
def test_create_board():
    repo = FakeRepo()
    service = BoardService(repo)

    user = FakeUser(1)
    payload = Payload()

    result = service.create_board(payload=payload, current_user = user)

    assert result.name == "Test Board"
    assert result.owner_id == 1

class FakeBoard:
    def __init__(self, name, owner_id):
        self.name = name
        self.owner_id = owner_id


def test_get_my_boards():
    repo = FakeRepo()
    service = BoardService(repo)

    user = FakeUser(1)

    repo.boards.append(FakeBoard("Board1", 1))

    result = service.get_my_boards(user)

    assert len(result) == 1
    assert result[0].name == "Board1"