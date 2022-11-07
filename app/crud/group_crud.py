from typing import Optional, List

from sqlalchemy.orm import Session
from sqlalchemy import select, update, desc, asc, func

from app.crud.base import CRUDBase
from app.models.group import Group
from app.schemas.group import CreateGroup, UpdateGroup


class CRUDGroup(CRUDBase[Group, CreateGroup, UpdateGroup]):
    pass


group_crud = CRUDGroup(Group)
