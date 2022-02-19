from os import error
from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from app.db import db
from app.db import userSchemas
from app.db import models
from app.utils.utils import Hashing, Validation


router = APIRouter(prefix="/api/v1/auth", tags=["Authentication"])

# create sub dependency for /register


async def get_current_user(user: userSchemas.UserResponseDetails = Depends(OAuth2PasswordRequestForm)):
    pass


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=userSchemas.UserResponse,  summary="Register user")
async def user_register(user: userSchemas.UserCreate, db: Session = Depends(db.get_db)):

    # Serverside validation of data using Validation class in utils

    # if not query == user.email:
    #     return HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'User with that email already exists!')

    # Check if unique key already exists

    # Hash password using bcrypt using Hashing class in utils
    hashed_password = Hashing.hash_password(user.password)
    user.password = hashed_password

    # Encrypt data using rsa encryption Encryption class in utils
    # Save hashed password & encrypted data in database
    # return decrypted response model

    try:

        new_user = models.User(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        # if is_verified = False HTTPRedirect to /verify

        return new_user
    except error:
        return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'{error}')


@ router.post("/verify")
async def registration_verify():
    #

    pass


@ router.post("/login")
async def user_login():
    pass


@ router.post("/forgot/{email}")
async def forgot_password():
    # Wanna get user ID

    pass
