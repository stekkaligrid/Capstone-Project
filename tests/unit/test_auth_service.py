from app.services.auth_service import AuthService
from fastapi import HTTPException

class FakeUser:

    def __init__(self,email,password_hash):
        self.email = email
        self.password_hash = password_hash

class FakeRepo:

    def __init__(self, user=None):
        self.user = user

    def get_by_email(self,email):
        return self.user
    
def fake_verify_password(plain,hashed):
    return plain == hashed

def fake_create_token(data):
    return "fake_token"

def test_login_success(monkeypatch):
    user = FakeUser("test@gmail.com","123456789")
    repo = FakeRepo(user)

    service = AuthService(repo)

    monkeypatch.setattr(
        "app.services.auth_service.verify_password",
        fake_verify_password
    )

    monkeypatch.setattr(
        "app.services.auth_service.create_access_token",
        fake_create_token
    )
    
    result = service.login("test@gmail.com","123456789")

    assert result["access_token"] == "fake_token"

def test_login_wrong_password(monkeypatch):
    user = FakeUser("test@gmail.com","123456789")
    repo = FakeRepo(user)

    service = AuthService(repo)

    monkeypatch.setattr(
        "app.services.auth_service.verify_password",
        fake_verify_password
    )

    try:
        service.login("test@gmail.com","wrongpass")
        assert False
    except HTTPException as e:
        assert e.status_code == 401