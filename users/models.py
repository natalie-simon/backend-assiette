from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    username: str
    email: Optional[str] = None
    #full_name: Optional[str] = None
    disabled: Optional[bool] = None
    rols: Optional[List[str]] = []

class UserInDb(User):
    hashed_password: str

class UserCreate(BaseModel):
    username: str
    email: str
    full_name: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str