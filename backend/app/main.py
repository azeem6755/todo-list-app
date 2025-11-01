from fastapi import FastAPI, HTTPException
from .config import get_settings
from .router import user, auth, task


app = FastAPI(title=get_settings().APP_NAME, root_path='/todo/')

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(task.router)