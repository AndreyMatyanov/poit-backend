from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# from app.config.settings import settings

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://postgres:admin@localhost:5432/postgres"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

