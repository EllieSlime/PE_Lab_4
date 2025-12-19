from sqlalchemy.orm import Session
from app.repositories.student_repository import StudentRepository
from app.repositories.group_repository import GroupRepository

class StudentService:
    def __init__(self):
        self.student_repo = StudentRepository()
        self.group_repo = GroupRepository()

    def add_to_group(self, db: Session, student_id: int, group_id: int):
        student = self.student_repo.get(db, student_id)
        return self.student_repo.add_to_group(db, student, group_id)

    def remove_from_group(self, db: Session, student_id: int):
        student = self.student_repo.get(db, student_id)
        return self.student_repo.remove_from_group(db, student)

    def transfer_group(self, db: Session, student_id: int, new_group_id: int):
        student = self.student_repo.get(db, student_id)
        return self.student_repo.add_to_group(db, student, new_group_id)
