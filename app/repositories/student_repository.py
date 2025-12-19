from sqlalchemy.orm import Session
from app.db.models import Student


class StudentRepository:
    def create(self, db: Session, name: str) -> Student:
        student = Student(name=name)
        db.add(student)
        db.commit()
        db.refresh(student)
        return student

    def get(self, db: Session, student_id: int):
        return db.query(Student).filter(Student.id == student_id).first()

    def delete(self, db: Session, student: Student):
        db.delete(student)
        db.commit()

    def list(self, db: Session):
        return db.query(Student).all()

    def add_to_group(self, db: Session, student: Student, group_id: int):
        student.group_id = group_id
        db.commit()
        db.refresh(student)
        return student

    def remove_from_group(self, db: Session, student: Student):
        student.group_id = None
        db.commit()
        db.refresh(student)
        return student
