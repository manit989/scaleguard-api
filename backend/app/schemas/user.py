from pydantic import BaseModel, ConfigDict
from uuid import UUID

class UserSchema(BaseModel):
    id: UUID
    username: str
    email: str

    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True
    )

class UserCreate(BaseModel):
    username : str
    email : str
    password : str
