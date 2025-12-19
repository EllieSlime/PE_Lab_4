from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.student import StudentCreate, StudentOut
from app.repositories.student_repository import StudentRepository

router = APIRouter(prefix="/students", tags=["Students"])
repo = StudentRepository()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=StudentOut)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    return repo.create(db, student.name)


@router.get("/", response_model=list[StudentOut])
def list_students(db: Session = Depends(get_db)):
    return repo.list(db)
