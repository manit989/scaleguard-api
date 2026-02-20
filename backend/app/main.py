from fastapi import FastAPI 
from app.db.userAuth import *
from app.api import auth
from app.api import users
from app.api import register

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(register.router)

@app.get("/")
async def hello():
    return {"message": "bkl idhr kya dekh rha h baki api test kr"}
