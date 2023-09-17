from typing import Optional

from pydantic import BaseModel


# Shared properties
class PostBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class ItemCreate(PostBase):
    pass


# Properties to receive on item update
class ItemUpdate(PostBase):
    pass


# Properties shared by models stored in DB
class ItemInDBBase(PostBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Item(ItemInDBBase):
    pass


# Properties properties stored in DB
class ItemInDB(ItemInDBBase):
    pass
