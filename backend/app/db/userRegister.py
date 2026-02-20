import os

from sqlalchemy import create_engine, Null, select, String, insert
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import User


engine = create_engine(str(os.getenv("SQLALCHEMY_URL")))
session = Session(engine)

async def createUser(newUser : dict):
    with engine.connect() as conn:
        result = conn.execute(
            insert(User),
            [
                newUser
            ],
        )
        conn.commit()

