from fastapi_pagination import Page
from pydantic import parse_obj_as
from sqlalchemy.orm import Session

from app.crud.publication_crud import publication_crud
from app.schemas.publication import CreatePublication, Publication, PublicationParams
from app.models.publication import Publication as PublicationModel


def create_publication(db: Session, publication_create: CreatePublication):
    publication_db = publication_crud.create(db=db, obj_in=publication_create)
    return parse_obj_as(Publication, publication_db)


def get_publications(db: Session):
    publications_db = publication_crud.get_multi(db=db)
    return [parse_obj_as(Publication, publication_db) for publication_db in publications_db]


def get_publication_by_id(db: Session, publication_id: int):
    publication_db = publication_crud.get(db=db, id=publication_id)
    return parse_obj_as(Publication, publication_db)


def search_publications(db: Session, params: PublicationParams):
    paginated_publication: Page[PublicationModel] = publication_crud.search_publication(db=db, params=params)
    paginated_publication.items = [Publication.from_orm(publication_db) for publication_db in paginated_publication.items]
    return paginated_publication
