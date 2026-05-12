from fastapi.testclient import TestClient
from main import app
import uuid

client = TestClient(app)


def create_user_get_token():

    unique_email = f"test_{uuid.uuid4()}@gmail.com"

    register_response = client.post(
        "/register",
        json={
            "email": unique_email,
            "password": "123456789",
            "first_name": "test",
            "last_name": "user",
        }
    )

    assert register_response.status_code == 200

    login_response = client.post(
        "/login",
        json={
            "email": unique_email,
            "password": "123456789",
        }
    )

    assert login_response.status_code == 200

    return login_response.json()["access_token"]

def test_login_success():

    unique_email = f"test_{uuid.uuid4()}@gmail.com"

    register_response = client.post(
        "/register",
        json={
            "email": unique_email,
            "password": "123456789",
            "first_name": "test",
            "last_name": "user",
        }
    )

    assert register_response.status_code == 200

    login_response = client.post(
        "/login",
        json={
            "email": unique_email,
            "password": "123456789",
        }
    )

    token = login_response.json()["access_token"]

    assert login_response.status_code == 200

    login_data = login_response.json()

    assert "access_token" in login_data
    assert login_data["token_type"] == "bearer"

def test_create_board():

    token = create_user_get_token()

    board_response = client.post(
        "/boards",
        json={"name": "Test Board"},
        headers={
            "Authorization": f"Bearer {token}"
            }
    )

    assert board_response.status_code == 200

    board_data = board_response.json()

    assert board_data["name"] == "Test Board"

def test_get_boards():

    token = create_user_get_token()
    headers = {
        "Authorization" : f"Bearer {token}"
        }

    client.post(
        "/boards",
        json={"name": "Board 1"},
        headers=headers
    )

    get_board = client.get(
        "/boards",
        headers=headers
    )

    assert get_board.status_code == 200
    data = get_board.json()
    assert isinstance(data,list)
    assert len(data)>=1

def test_create_section():

    token = create_user_get_token()

    headers = {"Authorization": f"Bearer {token}"}

    board_response = client.post(
        "/boards",
        json={"name": "Test Board"},
        headers=headers
    )

    assert board_response.status_code == 200

    board_id = board_response.json()["id"]

    section_response = client.post(
        f"/boards/{board_id}/sections",
        json={
            "name": "ToDo",
            "description": "Test Section"
            },
        headers=headers
    )
    assert section_response.status_code == 200

    data = section_response.json()

    assert data["name"] == "ToDo"

def test_create_ticket():

    token = create_user_get_token()

    headers = {"Authorization": f"Bearer {token}"}

    board_response = client.post(
        "/boards",
        json={"name": "Board 2"},
        headers=headers
    )

    assert board_response.status_code == 200

    board_id = board_response.json()['id']

    section_response = client.post(
        f"/boards/{board_id}/sections",
        json={
            "name": "Todo",
            "description": "Section testing"
            },
            headers=headers
    )

    assert section_response.status_code == 200

    data = section_response.json()

    assert data["name"] == "Todo"

    section_id = data["id"]

    ticket_response = client.post(
        f"/sections/{section_id}/tickets",
        json={
            "name": "Test name",
            "description": "Test description"
        },
        headers=headers
    )

    assert ticket_response.status_code == 200

    ticket_data = ticket_response.json()

    assert ticket_data["name"] == "Test name"

def test_get_tickets():

    token = create_user_get_token()

    headers = {"Authorization": f"Bearer {token}"}

    board_response = client.post(
        "/boards",
        json={"name": "Test Board"},
        headers=headers
    )

    assert board_response.status_code == 200

    board_id = board_response.json()["id"]

    section_response = client.post(
        f"/boards/{board_id}/sections",
        json={
            "name": "Todo",
            "description": "Test Section"
        },
        headers=headers
    )
    
    assert section_response.status_code == 200

    section_id = section_response.json()["id"]

    ticket_response = client.post(
        f"/sections/{section_id}/tickets",
        json={
            "name": "Test Ticket",
            "description": "Test description"
        },
        headers=headers
    )
    
    assert ticket_response.status_code == 200

    ticket_res = client.get(
        f"/sections/{section_id}/tickets",
        headers=headers
    )

    assert ticket_res.status_code == 200

    data = ticket_res.json()

    assert isinstance(data,list)
    assert len(data)>=1