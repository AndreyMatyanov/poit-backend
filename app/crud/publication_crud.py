from typing import Optional, List

from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session
from sqlalchemy import select, update, desc, asc, func

from app.crud.base import CRUDBase
from app.models.publication import Publication
from app.schemas.base import OrderingType
from app.schemas.publication import CreatePublication, UpdatePublication, PublicationParams


class CRUDPublication(CRUDBase[Publication, CreatePublication, UpdatePublication]):

    def search_publication(self, db: Session, params: PublicationParams):
        query = db.query(self.model)
        func_ordering = desc if params.sort == OrderingType.DESC else asc
        if params.title:
            query = query.filter(self.model.title.ilike(f'%{params.title}%'))
        if params.author_id:
            query = query.filter(self.model.author_id == params.author_id)
        query = query.order_by(func_ordering(self.model.title))
        return paginate(query, params)


publication_crud = CRUDPublication(Publication)
