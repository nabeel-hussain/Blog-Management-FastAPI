from typing import Union
from fastapi import FastAPI

from app.api.api_v1.api import api_router
from app.core.config import settings
from app.database.base import Base
from app.database.session import engine
Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(api_router, prefix=settings.API_V1_STR)
