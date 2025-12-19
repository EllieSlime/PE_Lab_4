from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.group import GroupCreate, GroupOut
from app.repositories.group_repository import GroupRepository

router = APIRouter(prefix="/groups", tags=["Groups"])
repo = GroupRepository()


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
