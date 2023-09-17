from datetime import datetime, timedelta
from typing import Any, Union

import bcrypt


# from app.core.config import settings


ALGORITHM = "HS256"


# def create_access_token(
#     subject: Union[str, Any], expires_delta: timedelta = None
# ) -> str:
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(
#             minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
#         )
#     to_encode = {"exp": expire, "sub": str(subject)}
#     encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(rounds=15))
