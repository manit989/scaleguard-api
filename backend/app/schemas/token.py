from pydantic import BaseModel
import uuid

class TokenData(BaseModel):
    id: uuid.UUID | None = None


class Token(BaseModel):
    access_token: str
    token_type: str

