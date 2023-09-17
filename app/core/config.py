from pydantic_settings import  BaseSettings,SettingsConfigDict
from pydantic import PostgresDsn
from typing import Optional

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = ""
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SQLALCHEMY_DATABASE_URI: str= None        
    
    
    model_config = SettingsConfigDict(env_file="app/.env")





settings = Settings()