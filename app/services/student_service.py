from sqlalchemy.orm import Session
from app.repositories.student_repository import StudentRepository
from app.repositories.group_repository import GroupRepository


class StudentService:
    def __init__(self):
        self.student_repo = StudentRepository()
        self.group_repo = GroupRepository()

    def add_to_group(self, db: Session, student_id: int, group_id: int):
        student = self.student_repo.get(db, student_id)
        group = self.group_repo.get(db, group_id)
        student.group = group
        db.commit()
        return student
