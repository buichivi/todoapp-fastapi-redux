from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from uuid import uuid4, UUID

router = APIRouter()

class TodoBase(BaseModel):
    title: str 
    description: str
    is_completed: bool = False
    
class Todo(TodoBase):
    id: UUID
    
todos: list[Todo] = [
    Todo(id=uuid4(),title="Do homework",description="Japanese's homework",is_completed=False)
]

@router.get('', response_model=list[Todo], status_code=status.HTTP_200_OK)
async def get_all_todos():
    """
    Get all todos
    """
    return todos

@router.get('/{id}', response_model=Todo, status_code=status.HTTP_200_OK)
async def get_todo_by_id(id: UUID):
    """
    Get todo by id
    """
    todo = [t for t in todos if t['id'] == id]
    if len(todo) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return todo[0]

@router.post('', response_model=Todo, status_code=status.HTTP_201_CREATED)
async def create_todo(todo_in: TodoBase):
    """
    Create todo
    """
    todo_create = Todo(id=uuid4(), **todo_in.model_dump())
    todos.append(todo_create)
    return todo_create

@router.put('/{id}', response_model=Todo, status_code=status.HTTP_200_OK)
async def update_todo(id: UUID, todo_in: TodoBase):
    """
    Update todo
    """
    
    for index, todo in enumerate(todos):
        if todo.id == id:    
            update_data = todo_in.model_dump(exclude_unset=True)
            todos[index] = todo.model_copy(update=update_data)
            return todos[index]
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

@router.delete('/{id}', status_code=status.HTTP_200_OK)
async def delete_todo(id: UUID):
    """
    Delete todo by id
    """
    for index, todo in enumerate(todos):
        if todo.id == id:
            deleted_todo = todos.pop(index)
            return {
                "message": "Deleted todo successfully!",
                "todo": deleted_todo
            }
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")