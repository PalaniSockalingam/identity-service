from fastapi import APIRouter
from models.user_identity import User
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId


router = APIRouter()

#GET Request method:
@router.get("/")
async def get_users():
    users = list_serial(collection_name.find())
    return users

@router.post("/user")
async def post_user(user: User):
    collection_name.insert_one(dict(user))

@router.put("/user/{id}")
async def put_user(id: str, user: User):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})

@router.delete("/user/{id}")
async def delete_user(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})