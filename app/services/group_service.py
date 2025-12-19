from sqlalchemy.orm import Session
from app.repositories.group_repository import GroupRepository
from app.repositories.student_repository import StudentRepository
from fastapi import HTTPException, status


class GroupService:
    def __init__(self):
        self.group_repo = GroupRepository()
        self.student_repo = StudentRepository()

    def create_group(self, db: Session, name: str):
        return self.group_repo.create(db, name)

    def get_group(self, db: Session, group_id: int):
        group = self.group_repo.get(db, group_id)
        if not group:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Group not found"
            )
        return group

    def delete_group(self, db: Session, group_id: int):
        group = self.get_group(db, group_id)
        db.delete(group)
        db.commit()

    def list_groups(self, db: Session):
        return self.group_repo.list(db)

    def get_students_in_group(self, db: Session, group_id: int):
        group = self.get_group(db, group_id)
        return group.students

    def transfer_student(
        self,
        db: Session,
        student_id: int,
        from_group_id: int,
        to_group_id: int
    ):
        student = self.student_repo.get(db, student_id)
        if not student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found"
            )

        if student.group_id != from_group_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Student is not in source group"
            )

        target_group = self.group_repo.get(db, to_group_id)
        if not target_group:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Target group not found"
            )

        student.group = target_group
        db.commit()
        db.refresh(student)
        return student
