from fastapi import FastAPI, Path, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Annotated
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get(path='/', response_class=HTMLResponse)
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/users/{user_id}", response_class=HTMLResponse)
async def get_one_user(request: Request, user_id: int) -> HTMLResponse:
    if user_id < 0 or user_id >= len(users):
        raise HTTPException(status_code=404, detail="User is not found")
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.post(path='/user/{username}/{age}')
async def post_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                    age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> User:
    new_id = (users[-1].id + 1) if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put(path='/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')],
                      username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username')],
                      age: Annotated[int, Path(ge=18, le=120, description='Enter age')]) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user

    else:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete(path='/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID')]) -> User:
    for i, user in enumerate(users):
        if user.id == user_id:
            return users.pop(i)

    else:
        raise HTTPException(status_code=404, detail='User was not found')
