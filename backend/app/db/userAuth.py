import os

from sqlalchemy import create_engine, Null, select, String, insert
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import User
from pwdlib import PasswordHash
from uuid import UUID, uuid4

password_hash = PasswordHash.recommended()

engine = create_engine(str(os.getenv("SQLALCHEMY_URL")))

session = Session(engine)

async def getUserByUuid(uuid: UUID):
    user : User = session.get(User,uuid)
    return user
    
async def getUserByUsername(username: str):
    user : User | None = session.scalars(select(User).where(User.username.__eq__(username))).one_or_none()
    return user

