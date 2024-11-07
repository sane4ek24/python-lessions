from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def main_page() -> str:
    return "Главная страница"


@app.get('/user/admin')
async def admin_login() -> str:
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def us_id(user_id: str) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@app.get('/user')
async def user_data(username: str, age: int) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
