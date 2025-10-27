from pydantic import BaseModel, EmailStr, conint, ConfigDict
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    model_config = ConfigDict(from_attributes=True)


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    username: str
    password: str

    model_config = ConfigDict(from_attributes=True)

class TaskBase(BaseModel):
    content: str
    deadline: Optional[datetime] = None
    completed: bool = False

    model_config = ConfigDict(from_attributes=True)

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    owner_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TaskOut(BaseModel):
    Task: Task
    completed: bool

    model_config = ConfigDict(from_attributes=True)


class TaskMarkComplete(BaseModel):
    task_id: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
