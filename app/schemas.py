from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True

class TicketBase(BaseModel):
    title: str
    description: str
    platform: str
    restaurant_branch: str
    username: str 

class TicketCreate(TicketBase):
    pass

class TicketUpdate(TicketBase):
    title: Optional[str] = None
    description: Optional[str] = None
    platform: Optional[str] = None
    restaurant_branch: Optional[str] = None
    username: Optional[str] = None
    status: Optional[str] = None

class Ticket(TicketBase):
    id: int
    status: str
    user_id: int
    platform: str
    restaurant_branch: str
    username: str
    created_at: datetime
    updated_at: datetime

class CommentBase(BaseModel):
    text: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    ticket_id: int
    user_id: Optional[int] = None
    created_at: datetime

    class Config:
        orm_mode = True
