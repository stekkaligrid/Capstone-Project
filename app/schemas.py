from pydantic import BaseModel,EmailStr,Field

class UserCreate(BaseModel):
    email : EmailStr
    password : str = Field(min_length=8, max_length=72)
    first_name :str
    last_name : str

class UserResponse(BaseModel):
    id : int
    email : str
    first_name : str
    last_name : str

    class Config:
        from_attributes = True

