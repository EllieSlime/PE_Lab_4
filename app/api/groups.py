from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.group import GroupCreate, GroupOut
from app.repositories.group_repository import GroupRepository
from app.services.group_service import GroupService

router = APIRouter(prefix="/groups", tags=["Groups"])
repo = GroupRepository()
service = GroupService()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=GroupOut)
def create_group(group: GroupCreate, db: Session = Depends(get_db)):
    return repo.create(db, group.name)


@router.get("/", response_model=list[GroupOut])
def list_groups(db: Session = Depends(get_db)):
    return repo.list(db)


@router.get("/{group_id}", response_model=GroupOut)
def get_group(group_id: int, db: Session = Depends(get_db)):
    group = repo.get(db, group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group


@router.delete("/{group_id}", response_model=dict)
def delete_group(group_id: int, db: Session = Depends(get_db)):
    group = repo.get(db, group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    repo.delete(db, group)
    return {"detail": "Group deleted"}


@router.get("/{group_id}/students", response_model=list)
def get_students_in_group(group_id: int, db: Session = Depends(get_db)):
    return service.get_students(db, group_id)
