from fastapi import APIRouter, HTTPException, status

from database.connection import Database

from models.users import User, UserSignIn

user_router = APIRouter(
    tags=["Users"]
)

user_database = Database(User)

@user_router.post("/signup")
async def sign_user_up(data: User) -> dict:
    user_exists = await User.find_one(User.email == data.email)

    if user_exists:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "User with provided email exists already"
        )
    
    await user_database.save(data)

    return {
        "status": "success",
        "message": "User created successfully"
    }

@user_router.post("/signin")
async def sign_user_in(data: UserSignIn) -> dict:
    user_exists = await User.find_one(User.email == data.email)
    
    if not user_exists:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "User with provided email doesn't exist"
        )

    if user_exists.password != data.password:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Credential invalid"
        )
    
    return {
        "status": "success",
        "message": "User signed in successfully"
    }