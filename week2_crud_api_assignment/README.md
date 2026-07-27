# Task API

A small CRUD API that manages an in-memory to-do list. Built for the FlyRank Internship Backend Track.

## How to Run

1. Install dependencies: `pip install fastapi uvicorn pydantic`
2. Start the server: `uvicorn main:app --reload`
3. The API will be available at `http://localhost:8000`.

## Endpoints

| Operation | Method | Endpoint | Description |
| :--- | :--- | :--- | :--- |
| **Create** | POST | `/tasks` | Add a new task |
| **Read All** | GET | `/tasks` | List all tasks |
| **Read One** | GET | `/tasks/{id}` | Get a specific task by ID |
| **Update** | PUT | `/tasks/{id}` | Change a task's title or status |
| **Delete** | DELETE | `/tasks/{id}` | Remove a task |


![Swagger UI Screenshot](https://github.com/user-attachments/assets/fdcde219-ce37-4085-a90b-a7fb13410472)

## Sample Request

```bash
curl -i -X POST http://localhost:8000/tasks \
-H "Content-Type: application/json" \
-d '{"title":"Buy milk"}'
