import pydantic
import pytest
from meowpi.database.mongo import *
from pymongo_inmemory import MongoClient


@pytest.fixture
def user_data():
    payload = {
        'full_name': 'Abluble de Almeida',
        'birth_date': 10/10/1992,
        'email': 'abluble@gmail.com',
        'username': 'AbluCat',
        'password': 'Ablu123',
        'hashed_password': 'ablu123ablu123',
        'cats': [],
    }
    instancepayload = CreateUserSchema(**payload)
    return instancepayload

@pytest.mark.asyncio
async def test_get_user_valid(user_data):
    client_test = MongoClient()
    db_test = MongoDatabase(client_test)
    new_test_user = await db_test.create_user(user_data)
    test_get_user = await db_test.get_user('AbluCat')
    assert test_get_user
    print(test_get_user)
