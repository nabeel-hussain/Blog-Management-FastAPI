from fastapi import APIRouter

from app.api.api_v1.endpoints import posts, security, users

api_router = APIRouter()
api_router.include_router(security.router, prefix="/security",tags=["Security"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(posts.router, prefix="/posts", tags=["Posts"])
