from sqlalchemy.orm import Session
from app.db.models import Group


class GroupRepository:
    def create(self, db: Session, name: str) -> Group:
        group = Group(name=name)
        db.add(group)
        db.commit()
        db.refresh(group)
        return group

    def get(self, db: Session, group_id: int):
        return db.query(Group).filter(Group.id == group_id).first()

    def delete(self, db: Session, group: Group):
        db.delete(group)
        db.commit()

    def list(self, db: Session):
        return db.query(Group).all()
