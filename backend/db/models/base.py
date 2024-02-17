from ast import List
from typing import Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, Column, String

meta_data = DeclarativeBase.metadata

class PrimaryBase(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    created_by: Mapped[int] = relationship(
    cascade="all, delete-orphan"
    )