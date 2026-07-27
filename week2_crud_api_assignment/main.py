from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Task API", version="1.0")

# Stage 2: In-memory list pre-filled with 3 tasks
tasks = [
    {"id": 1, "title": "Buy milk", "done": False},
    {"id": 2, "title": "Read HTTP overview", "done": True},
    {"id": 3, "title": "Learn FastAPI", "done": False}
]
next_id = 4

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None

# Stage 1: Root and health endpoints
@app.get("/")
def get_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health")
def health_check():
    return {"status": "ok"}

# Stage 2: Read endpoints
@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{id}")
def get_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
    return JSONResponse(status_code=404, content={"error": f"Task {id} not found"})


# Stage 3: Create endpoint
@app.post("/tasks", status_code=201)
def create_task(task_in: TaskCreate):
    global next_id
    if not task_in.title.strip():
        return JSONResponse(status_code=400, content={"error": "Title cannot be empty"})

    new_task = {"id": next_id, "title": task_in.title, "done": False}
    tasks.append(new_task)
    next_id += 1
    return new_task

