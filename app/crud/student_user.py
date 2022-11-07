from sqlalchemy.orm import with_polymorphic, Session

from app.crud.base import CRUDBase
from app.models.group import Group
from app.models.user_student import UserStudent
from app.models.users import User
from app.schemas.user import UserStudentCreate, UserStudentUpdate

student_user_model = with_polymorphic(User, [UserStudent])


class CRUDUserStudent(CRUDBase[student_user_model, UserStudentCreate, UserStudentUpdate]):
    def get_users_students_by_group_id(self, db: Session, group_id: int):
        student_user_db = db.query(UserStudent).filter(UserStudent.group_id == group_id).all()
        return student_user_db


user_student_crud = CRUDUserStudent(UserStudent)
