import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config.settings import settings
from app.db.database import Base

@pytest.fixture
def app_settings():
    return settings.settings

@pytest.fixture
def db(postgresql):
    connection = f'postgresql+psycopg2://{postgresql.info.user}:@{postgresql.info.host}:{postgresql.info.port}/{postgresql.info.dbname}'

    engine = create_engine(
        connection,
        connect_args={'options': '-csearch_path={}'.format('public')}
    )

    SessionLocalPytest = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(engine)
    session = SessionLocalPytest()
    yield session
    session.close()



# @pytest.fixture(scope="function")
# def db():
#     connection = f'postgresql+psycopg2://{settings.db_user}:{settings.db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}'
#     engine = create_engine(  # noqa
#         connection, connect_args={'options': '-csearch_path={}'.format('public')}
#     )
#     TestingSessionLocal = sessionmaker(
#         autocommit=False, autoflush=False, bind=engine
#     )
#     Base.metadata.create_all(bind=engine)
#     session = TestingSessionLocal()
#     yield session
#     session.close()
#     Base.metadata.drop_all(bind=engine)
