from fastapi import APIRouter, HTTPException, status

from models.users import User, UserSignIn

user_router = APIRouter(
    tags=["Users"]
)

users = {}

@user_router.post("/signup")
async def sign_user_up(data: User) -> dict:
    if data.email in users:
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = "User with supplied username already exists".
        )

    users[data.email] = data

    return {
        "message": "user successfully registered!"
    }

@user_router.post("/signin")
async def sign_user_in(data: UserSignIn) -> dict:
    if data.email not in users:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "User doesn't exist".
        )

    if data.password != users[data.email].password:
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail="Wrong credential passed"
        )

    return {
        "message": "User signed in successfully"
    }