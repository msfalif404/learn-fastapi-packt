from pydantic import BaseModel, EmailStr

class User(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "orang1@gmail.com",
                "password": "ABCD1234"
            }
        }

class UserSignIn(BaseModel):
    email: EmailStr,
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "orang1@gmail.com",
                "password": "ABCD1234"
            }
        }