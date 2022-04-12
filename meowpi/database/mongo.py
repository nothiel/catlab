from pymongo import MongoClient

from meowpi.services.users import UserSchema
from meowpi.utils.errors import UserNotFoundError




class MongoDatabase:
    def __init__(self, client) -> None:
        self.client = client
        self.database = self.client['catlab']
        self.coll = self.database['users']

    async def get_username(self, username: str) -> UserSchema:
        user = self.coll.find_one({'username': username})
        if not user:
            raise UserNotFoundError(f"User with username {username} was not found")
        return UserSchema(**user)


client = MongoClient('mongodb://root:MongoDB2019!@localhost:27017')

mongo_database = MongoDatabase(client)