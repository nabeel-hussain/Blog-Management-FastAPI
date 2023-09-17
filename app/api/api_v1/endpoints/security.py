from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from app.api import deps
from app import crud,schemas
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/login",response_model=schemas.User)
def login(
    *,
    db: Session = Depends(deps.get_db),
    user_login: schemas.user.UserLogin
):
    user = crud.user.authenticate(db=db,email=user_login.email,password=user_login.password)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="Login Failed, Either username or password is incorrect",
        )
    return user

    