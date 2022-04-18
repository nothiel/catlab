from fastapi import FastAPI
from database.mongo import mongo_database
from models.users import CreateUserSchema
from error_handler import setup_exception_handlers

app = FastAPI()



@app.get('/')
async def meow_world():
    return {'Meow': 'World'}

@app.get('/{username}')
async def get_user(username: str):
    user = await mongo_database.get_user_by_username(username)
    return user

@app.post('/user')
async def create_user(create_user_data: CreateUserSchema):
    user_id = await mongo_database.create_user(create_user_data)
    return user_id

setup_exception_handlers(app)