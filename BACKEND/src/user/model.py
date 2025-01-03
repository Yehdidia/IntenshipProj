from sqlmodel import SQLModel, Field
from pydantic import BaseModel
import uuid


class Users(SQLModel, table=True):
    user_uuid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(index=True)
    surname: str | None = Field(default=None, index=True)  # Correction: int -> str pour "surname"
    access_code: str  # Correction de "acceess_code" à "access_code"
    email: str
