from pydantic import BaseModel, EmailStr
from datetime import datetime

from pydantic.types import conint



class PostBase(BaseModel):
    title:str
    content:str
    published: bool = True
    

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut
    
    class Config:
        orm_mode = True
        
class PostOut(BaseModel):
    Post: Post
    votes: int
    
    class Config:
        orm_mode = True
        
class UserBase(BaseModel):
    email: EmailStr
    password: str
    
    
class UserCreate(UserBase):
    pass

        
class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
    class Config:
        orm_mode = True
        
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: int | None = None
    
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)  # 0 or 1, where 1 means upvote and 0 means no vote
    
    class Config:
        orm_mode = True