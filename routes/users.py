from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from database.connection import Database

from models.users import User

from auth.hash_password import HashPassword
from auth.jwt_handler import create_access_token

user_router = APIRouter(
    tags=["Users"]
)

user_database = Database(User)
hash_password = HashPassword()

@user_router.post("/signup")
async def sign_user_up(data: User) -> dict:
    user_exists = await User.find_one(User.email == data.email)

    if user_exists:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "User with provided email exists already"
        )
    
    hashed_password = hash_password.create_hash(data.password)
    data.password = hashed_password
    await user_database.save(data)

    return {
        "status": "success",
        "message": "User created successfully"
    }

@user_router.post("/signin")
async def sign_user_in(data: OAuth2PasswordRequestForm = Depends()) -> dict:
    user_exists = await User.find_one(User.email == data.username)
    
    if not user_exists:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "User with provided email doesn't exist"
        )

    if not hash_password.verify_hash(data.password, user_exists.password):
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Credential Invalid"
        )
    
    access_token = create_access_token(user_exists.email)
    return {
        "status": "success",
        "message": "User signed in successfully",
        "access_token": access_token,
        "token_type": "Bearer",
    }