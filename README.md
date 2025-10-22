# Todo List App (FastAPI)

Small todo list REST API built with FastAPI, SQLModel and SQLAlchemy. The backend dependencies are listed in [backend/requirements.txt](backend/requirements.txt). The backend application code is in the [backend/app](backend/app) directory. See [.gitignore](.gitignore) for local ignore rules.

## Features
- Create, read, update, delete (CRUD) todos
- An authentication logic, which means you’ll have to keep a new table of users and their credentials
- You’ll have to create both users and tasks.
- You’ll also have to be able to update tasks (their status) and even delete them.
- Get a list of tasks, filter them by status and get the details of each one.
- Ready to run with Uvicorn or Hypercorn

## Requirements
- Python 3.10+
- Install dependencies:
```sh
pip install -r [requirements.txt](http://_vscodecontentref_/0)