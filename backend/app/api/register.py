from fastapi import APIRouter
from pwdlib import PasswordHash
from uuid import uuid4

from app.schemas.user import UserCreate
from app.models import *
import app.db.userRegister as ur

password_hash = PasswordHash.recommended()

router = APIRouter(prefix="/register",tags=["register"])

@router.post("/")
async def createUser(user: UserCreate):
    user_dict = user.model_dump()
    user_dict["id"] = uuid4()
    user_dict["password_hash"] = password_hash.hash(user_dict["password"])
    user_dict.pop("password")
    result = await ur.createUser(user_dict)
    return {}
