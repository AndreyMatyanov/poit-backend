from datetime import datetime
from typing import List

from fastapi import APIRouter, File, UploadFile, Depends
from fastapi_pagination import Page
from sqlalchemy.orm import Session

from app.api.depends import get_db
from app.config.settings import PUBLICATION_FILES_PATH, UPLOADED_FILES_PATH
from app.schemas.file import CreateFile, FileType
from app.schemas.publication import Publication, CreatePublication, PublicationParams, PublicationType
from app.service import file_service, publication_service
from app.service.file_service import format_filename, save_file_to_uploads, get_file_size

path = UPLOADED_FILES_PATH + PUBLICATION_FILES_PATH

router = APIRouter()


@router.post("/", response_model=Publication)
async def create_publication(
        title: str,
        author_id: int,
        description: str,
        publication_type: PublicationType,
        upload_file: UploadFile = File(...),
        db: Session = Depends(get_db)
):
    full_name = format_filename(upload_file)
    await save_file_to_uploads(file=upload_file, filename=full_name, path=path)
    file_size = get_file_size(full_name, path=path)
    file_create = CreateFile(
        name=full_name,
        size=file_size,
        mime_type=upload_file.content_type,
        modification_time=datetime.now(),
        file_type=FileType.PUBLICATION
    )
    file = await file_service.create_file(db=db, file_create=file_create, path=path)
    publication_create = CreatePublication(
        file_id=file.id,
        title=title,
        author_id=author_id,
        publication_type=publication_type,
        description=description,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    publication = publication_service.create_publication(db=db, publication_create=publication_create)
    return publication


@router.get("/", response_model=List[Publication])
def get_publications(db: Session = Depends(get_db)):
    publications = publication_service.get_publications(db=db)
    return publications


@router.get("/{publication_id}", response_model=Publication)
def get_publication_by_id(publication_id: int, db: Session = Depends(get_db)):
    publication = publication_service.get_publication_by_id(db=db, publication_id=publication_id)
    return publication


@router.post("/search", response_model=Page[Publication])
def search_publication(params: PublicationParams = Depends(), db: Session = Depends(get_db)):
    print('1')
    publications: Page[Publication] = publication_service.search_publications(db=db, params=params)
    return publications
