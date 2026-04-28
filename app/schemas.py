from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)
    first_name: str
    last_name: str


class UserResponse(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    email: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class BoardCreate(BaseModel):
    name: str
    description: str | None = None


class BoardResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    owner_id: int

    class Config:
        from_attributes = True


class BoardDetailResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    owner_id: int
    sections: list = []
    members: list = []
    invitations: str | None = None

    class Config:
        from_attributes = True


class SectionCreate(BaseModel):
    name: str
    description: str | None = None


class SectionResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    board_id: int

    class Config:
        from_attributes = True


class SectionUpdate(BaseModel):
    name: str
    description: str | None = None


class TicketCreate(BaseModel):
    name: str
    description: str | None = None
    assigned_to: int | None = None


class TicketResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    section_id: int
    board_id: int
    created_by: int
    assigned_to: int | None = None

    class Config:
        from_attributes = True


class TicketUpdate(BaseModel):
    name: str
    description: str | None = None
    assigned_to: int | None = None
    section_id: int
