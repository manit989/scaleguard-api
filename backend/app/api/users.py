from typing import Annotated 
from fastapi import APIRouter, Depends, HTTPException

from app.models import User
from app.api.auth import get_current_user
from app.helpers.rateLimit import limit_reached

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_user)],
    _ = Depends(limit_reached)
):
    return {"username": current_user.username,"email": current_user.email}

