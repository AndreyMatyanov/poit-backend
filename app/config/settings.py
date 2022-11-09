from decimal import Decimal
import os
from uuid import UUID

from pydantic import BaseSettings


class Settings(BaseSettings):
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str

    class Config:
        env_file = '.env'


settings = Settings(_env_file=os.getenv('APP_CONFIG'), _env_file_encoding='utf-8')

UPLOADED_FILES_PATH = "uploaded_files/"
PUBLICATION_FILES_PATH = "publications_files/"
AVATAR_FILES_PATH = "avatar_files/"
