from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    is_super: bool
    is_verified: bool
    created_at: datetime


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    phone: int
    address: str
    postal_code: int
    city: str
    country: str


class UserResponseDetails(UserBase):
    phone: int
    address: str
    postal_code: int
    city: str
    country: str

    class Config:
        orm_mode = True


class UserResponse(UserBase):
    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
