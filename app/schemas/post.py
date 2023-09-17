from typing import Optional

from pydantic import BaseModel


# Shared properties
class PostBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on Post creation
class PostCreate(PostBase):
    pass


# Properties to receive on Post update
class PostUpdate(PostBase):
    pass


# Properties shared by models stored in DB
class PostInDBBase(PostBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Post(PostInDBBase):
    pass


# Properties properties stored in DB
class PostInDB(PostInDBBase):
    pass
