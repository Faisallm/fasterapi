from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

# schema
# validates user submitted data
# sending and receiving data should be validated by a schema

class PostBase(BaseModel):
    title: str
    content: str
    # if a user doesn't provide a value,
    # it will default to true.
    published: bool = True



class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    # we added a new property called owner at runtime (monkey-patching)
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id : Optional[int] = None


class Vote(BaseModel):
    post_id: int
    # le: The value must be less than or equal to this.
    dir: conint(le=1)