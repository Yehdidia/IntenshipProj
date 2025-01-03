from sqlmodel import Field, SQLModel

class Role(SQLModel, table=True):
    role_id: int = Field(default=None, primary_key=True)
    role_name: str = Field(default=None, index=True)

class AccessCode(SQLModel, table=True):
    accessCode_id: int = Field(default=None, primary_key=True)
    accessCode_name: str = Field(default=None, index=True)

class User(SQLModel, table=True):
    user_id: int = Field(default=None, primary_key=True)
    name: str = Field(default=None, index=True)
    surname: str = Field(default=None, index=True)
    email: str = Field(default=None, index=True)
    post: str = Field(default=None, index= True)
    role_id: = int = Field(defalt=None, foreign_key="Role.role_id")
    accessCode: str = Field(defalt=None, index=True)


class Presence(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    arrivalTime: str = Field(default=None, index=True)
    departureTIme: str = Field(default=None, index=True)
    user_id: int = Field(default=None, index=True)