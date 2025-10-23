from sqlmodel import SQLModel, Field, Column, DateTime, ForeignKey
from typing import Optional, List, Annotated
from datetime import datetime
import sqlalchemy as sa
from .config import get_settings, timezone


settings = get_settings()


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True, max_length=255)
    email: str = Field(unique=True)
    password: str = Field(nullable=False, max_length=255)
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), default=datetime.now(timezone))
    )


class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    content: str = Field(nullable=False, max_length=255)
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), default=datetime.now(timezone))
    )
    deadline: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), nullable=True)
    )
    completed: bool = Field(default=False)
    owner_id: int = Field(nullable=False, foreign_key="user.id", ondelete="CASCADE")

    