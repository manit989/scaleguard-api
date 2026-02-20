import redis
import time

from app.api.auth import get_current_user
from app.models import User
from fastapi import Depends, HTTPException


redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

async def limit_reached(user: User = Depends(get_current_user)):
    if await is_rate_limited(str(user.id)):
        raise HTTPException(status_code=429, detail="Limit exceeded")
    return True

async def is_rate_limited(user_id: str):
    lua_file = 'app/helpers/lua/ratelimit.lua'
    with open(lua_file, 'r', encoding='utf-8') as file:
        result = redis_client.eval(file.read(), 1, f"limit:{user_id}", 1, 10, time.time())
    return result == 0
