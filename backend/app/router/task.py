from fastapi import Depends, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from .. import schemas, models
from ..database import get_db
from ..utils import get_current_user
from typing import List, Optional


router = APIRouter(prefix='/posts', tags=['Posts'])

@router.get('', response_model=List[schemas.Task], status_code=status.HTTP_200_OK)
async def get_tasks_for_user(db: Session = Depends(get_db), 
                             current_user: int = Depends(get_current_user), 
                             limit: int = 10, skip: int = 0, 
                             search: Optional[str] = ""):
    tasks_list = db.query(models.Task).filter(models.Task.owner_id == current_user.id).filter(
        models.Task.content.contains(search)).limit(limit).offset(skip).all()

    return tasks_list

@router.post('', response_model=schemas.Task, status_code=status.HTTP_201_CREATED)
async def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    print(task)
    new_task = models.Task(owner_id=current_user.id, **task.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
