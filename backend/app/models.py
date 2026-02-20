from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id : Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    username : Mapped[str] = mapped_column(String(50), unique=True)
    email : Mapped[str] = mapped_column(String(100), unique=True)
    password_hash : Mapped[str] = mapped_column(String(50), unique=True)


