from sqlalchemy.orm import Session
from . import models, schemas
from typing import Optional


def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_tasks_for_user(db: Session, user_id: int, limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    tasks_list = db.query(models.Task).filter(models.Task.owner_id == user_id).filter(
        models.Task.content.contains(search)).order_by(
        models.Task.id.desc()).limit(limit).offset(skip).all()
    return tasks_list

def create_task(db: Session, task: schemas.TaskCreate, user_id: int):
    new_task = models.Task(owner_id=user_id, **task.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def mark_task_as_complete(db: Session, task_id: int):
    task_to_mark = get_task(db, task_id)
    task_to_mark.completed = True
    db.commit()
    db.refresh(task_to_mark)
    return task_to_mark

