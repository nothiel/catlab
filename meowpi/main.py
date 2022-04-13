from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from meowpi.database.mongo import mongo_database
from meowpi.models.users import CreateUserSchema
from meowpi.utils.errors import UserNotFoundError


app = FastAPI()

@app.exception_handler(UserNotFoundError)
async def not_found_exception_handler(request: Request, exc: UserNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"message": f"User not found"},
    )

@app.get('/')
async def meow_world():
    return {'Meow': 'World'}

@app.get('/{username}')
async def get_user(username: str):
    user = await mongo_database.get_user_by_username(username)
    return user

@app.post('/user')
async def create_user(create_user_data: CreateUserSchema):
    return "aoba"