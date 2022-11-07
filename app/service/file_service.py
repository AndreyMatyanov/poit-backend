import os

from pydantic import parse_obj_as
from sqlalchemy.orm import Session
from starlette.responses import FileResponse

from app.config.settings import UPLOADED_FILES_PATH, PUBLICATION_FILES_PATH, AVATAR_FILES_PATH
from app.crud.file_crud import file_crud
from app.models.file import File as FileModel
from app.schemas.file import CreateFile, File as FileSchema, FileType


def delete_file_from_uploads(file_name, path):
    try:
        os.remove(path + file_name)
    except Exception as e:
        print(e)


async def save_file_to_uploads(file, filename, path):
    with open(f'{path}{filename}', "wb") as uploaded_file:
        file_content = await file.read()
        uploaded_file.write(file_content)
        uploaded_file.close()


def format_filename(file):
    filename, ext = os.path.splitext(file.filename)
    return filename + ext


def get_file_size(filename, path: str = None):
    file_path = f'{path}{filename}'
    return os.path.getsize(file_path)


def get_file_by_id(db: Session, file_id: int):
    file = file_crud.get(db=db, id=file_id)
    return file


async def create_file(db: Session, file_create: CreateFile, path: str):
    file_db: FileModel = file_crud.get_file_by_name(db=db, file_name=file_create.name)
    if not file_db:
        file_new_db = file_crud.create(db=db, obj_in=file_create)
        return parse_obj_as(FileSchema, file_new_db)
    if file_db:
        delete_file_from_uploads(file_db.name, path=path)
        file_new_db = file_crud.update(db=db, db_obj=file_db, obj_in=file_create)
        return parse_obj_as(FileSchema, file_new_db)


def download_file(db: Session, file_id: int):
    file_db = file_crud.get(db=db, id=file_id)

    path = UPLOADED_FILES_PATH

    if file_db.file_type == FileType.PUBLICATION:
        path += PUBLICATION_FILES_PATH
    elif file_db.file_type == FileType.AVATAR:
        path += AVATAR_FILES_PATH

    if file_db:
        file_resp = FileResponse(path + file_db.name,
                                 media_type=file_db.mime_type,
                                 filename=file_db.name)
        return file_resp
    else:
        return None


def delete_file(db: Session, file_id: int):
    file_db = file_crud.get(db=db, id=file_id)
    if file_db:
        file_crud.remove(db=db, id=file_db.id)
        path = UPLOADED_FILES_PATH

        if file_db.file_type == FileType.PUBLICATION:
            path += PUBLICATION_FILES_PATH
        elif file_db.file_type == FileType.AVATAR:
            path += AVATAR_FILES_PATH
        delete_file_from_uploads(file_name=file_db.name, path=path)
        return {'msg': f'File {file_db.name} successfully deleted'}
    else:
        return {'msg': f'File does not exist'}
