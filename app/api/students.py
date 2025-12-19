from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.student import StudentCreate, StudentOut
from app.repositories.student_repository import StudentRepository
from app.services.student_service import StudentService

router = APIRouter(prefix="/students", tags=["Students"])
repo = StudentRepository()
service = StudentService()

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


@router.get("/{student_id}", response_model=StudentOut)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = repo.get(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.delete("/{student_id}", response_model=dict)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = repo.get(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    repo.delete(db, student)
    return {"detail": "Student deleted"}


@router.post("/{student_id}/add_to_group/{group_id}", response_model=StudentOut)
def add_student_to_group(student_id: int, group_id: int, db: Session = Depends(get_db)):
    return service.add_to_group(db, student_id, group_id)


@router.post("/{student_id}/remove_from_group", response_model=StudentOut)
def remove_student_from_group(student_id: int, db: Session = Depends(get_db)):
    return service.remove_from_group(db, student_id)


@router.post("/{student_id}/transfer_group/{new_group_id}", response_model=StudentOut)
def transfer_student_group(student_id: int, new_group_id: int, db: Session = Depends(get_db)):
    return service.transfer_group(db, student_id, new_group_id)
