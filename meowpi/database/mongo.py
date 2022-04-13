from pymongo import MongoClient
from meowpi.models.cats import CatsSchema, CatSchema

from meowpi.models.users import CreateUserSchema, UserSchema, UserSensitiveData
from meowpi.utils.errors import DatabaseUpdateError, UserAlreadyCreated, UserNotFoundError

class MongoDatabase:
    def __init__(self, client) -> None:
        self.client = client
        self.database = self.client['catlab']
        self.coll = self.database['users']

    async def get_user(self, username: str) -> dict:
        user = self.coll.find_one({'username': username})
        if not user:
            raise UserNotFoundError(f"User with username {username} was not found")
        return user

    async def get_user_by_username(self, username: str) -> UserSchema:
        user = await self.get_user(username)
        return UserSchema(**user)

    async def get_full_user_by_username(self, username: str) -> UserSensitiveData:
        user = await self.get_user(username)
        return UserSensitiveData(**user)

    async def get_all_cats_by_username(self, username: str) -> CatsSchema:
        user = await self.get_user(username)
        catlist = user['cats']
        return CatsSchema(**catlist)

    async def create_user(self, user_data: CreateUserSchema ) -> str: 
        is_already_created = self.coll.count_documents({'username': user_data.username})
        if is_already_created:
            raise UserAlreadyCreated(f"User with username {user_data.username} is already created.")
        created_user_id = self.coll.insert_one(user_data).inserted_id
        created_user_id = str(created_user_id)
        return created_user_id
        
    async def update_user_data(self, username: str, update_data: dict) -> bool:
        is_already_created = self.coll.count_documents({'username': update_data.get('username')})
        if is_already_created:
            raise UserAlreadyCreated(f"User with username {update_data.get('username')} is already created.")
        
        is_modified = self.coll.update_one({'username': username}, {'$set': update_data}).modified_count
        if not is_modified:
            raise DatabaseUpdateError(f"Error while modifying username {username}")
        return True
    
    async def update_user_add_cats(self, username: str, cat: CatSchema) -> bool:
        add_cat = self.coll.update_one({'username': username},{'$push': {'cats': cat.dict()}}).modified_count
        if not add_cat:
            raise DatabaseUpdateError(f"Error while adding cat for {username}")
        return True

    async def delete_user(self, username: str) -> bool:
        is_user_exist = await self.get_user(username)
        if not is_user_exist:
            raise UserNotFoundError(f"User with username {username} was not found")
        is_deleted_user = self.coll.delete_one({'username': username}).deleted_count
        if is_deleted_user:
            return True 
        return False

       
client = MongoClient('mongodb://root:MongoDB2019!@localhost:27017')

mongo_database = MongoDatabase(client)