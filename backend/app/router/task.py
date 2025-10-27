from fastapi import Depends, Response, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from .. import schemas, models
from ..database import get_db
from ..utils import get_current_user
from typing import List, Optional
from .. import crud


router = APIRouter(prefix='/posts', tags=['Posts'])

@router.get('', response_model=List[schemas.Task], status_code=status.HTTP_200_OK)
async def get_tasks_for_user(db: Session = Depends(get_db), 
                             current_user: models.User = Depends(get_current_user),
                             limit: int = 10, skip: int = 0, 
                             search: Optional[str] = ""):
    tasks_list = crud.get_tasks_for_user(db, current_user.id, limit=limit, skip=skip, search=search)

    return tasks_list

@router.post('', response_model=schemas.Task, status_code=status.HTTP_201_CREATED)
async def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    new_task = crud.create_task(db, task, current_user.id)
    return new_task

@router.put('/mark-complete', response_model=schemas.Task, status_code=status.HTTP_200_OK)
async def mark_task_as_complete(task: schemas.TaskMarkComplete, db: Session = Depends(get_db),
                                current_user: int = Depends(get_current_user)):
    task_to_mark = crud.mark_task_as_complete(db, task_id=task.task_id)
    return task_to_mark



