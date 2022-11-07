from datetime import datetime

from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import FileResponse

from app.api.depends import get_db
from app.config.settings import UPLOADED_FILES_PATH, PUBLICATION_FILES_PATH
from app.service import file_service
from app.schemas.file import File as FileSchema, CreateFile
from app.service.file_service import format_filename, get_file_size, save_file_to_uploads

router = APIRouter()


# @router.post("/", status_code=status.HTTP_200_OK, response_model=FileSchema)
# async def upload_file(upload_file: UploadFile = File(...), db: Session = Depends(get_db)):
#     full_name = format_filename(upload_file)
#     await save_file_to_uploads(file=upload_file, filename=full_name, path=UPLOADED_FILES_PATH)
#     file_size = get_file_size(full_name)
#     file_create = CreateFile(
#         name=full_name,
#         size=file_size,
#         mime_type=upload_file.content_type,
#         modification_time=datetime.now()
#     )
#     print(file_create.name)
#     file = await file_service.create_file(db=db, file_create=file_create)
#     return file


@router.get("/")
async def download_file(file_id: int, db: Session = Depends(get_db)):
    file: FileResponse | None = file_service.download_file(file_id=file_id, db=db)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    return file


@router.delete("/{file_id}")
async def delete_file(file_id: int, db: Session = Depends(get_db)):
    msg = file_service.delete_file(db=db, file_id=file_id)
    return msg
