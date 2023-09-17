from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any,List
from app import crud,schemas
from app.api import deps
router = APIRouter()

@router.get("/",response_model=List[schemas.Post])
def get_posts(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int =100
) -> Any:
    """
    Retrieve Posts.
    """
    posts = crud.post.get_multi(db,skip=skip,limit=limit)
    return posts

@router.post("/",response_model=schemas.Post)
def add_post(
    *,
    db: Session = Depends(deps.get_db),
    post_in: schemas.PostCreate
) -> Any:
    """
    Create New Post
    """
    post = crud.post.create(db,obj_in=post_in)
    return post

@router.get("/{post_id}",response_model=schemas.Post)
def get_post_by_id(
    post_id: int,
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Get a post by Id
    """
    post = crud.post.get(db,id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="User not found")
    return post

