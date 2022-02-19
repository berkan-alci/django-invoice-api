import random
import string
from passlib.context import CryptContext
import re

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class IdGenerator:

    def generate_user_id():
        '''
        Generate a random user id format: ui_abcd_1
        '''

        user_id = "ui"
        user_id = user_id.join(random.choice(
            string.ascii_lowercase) for i in range(4))
        user_id.join(random.choice(string.digits))

        return user_id


class Hashing:

    def hash_password(password: str):
        '''
        Hash password using the bcrypt library
        '''
        return pwd_context.hash(password)

    def verify_password(plain_pass: str, hashed_pass: str):
        '''
        Compare plain password with hashed password.
        Returns True if it matches
        '''
        return pwd_context(plain_pass, hashed_pass)


class Validation:

    def validate_password(password: str):
        '''
        Serverside validation of password
        '''
        isValid = True

        if not isinstance(password, str):
            print("error here")
            isValid = False

        if 8 > password.length() < 20:
            print("error here")
            isValid = False

        return isValid

    def validate_email(email: str):
        '''
        Serverside validation of email
        '''
        isValid = True
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if not isinstance(email, str):
            isValid = False

        if not (re.fullmatch(regex, email)):
            isValid = False

        return isValid

    def validate_phone(phone: str):
        '''
        Serverside validation of phone number
        '''
        print("phone reached here 1")
        if not isinstance(phone, str):
            isValid = False
        print("phone reached here 2")

        if phone.length() != 11:
            isValid = False
        print("phone reached here 3")

        return isValid


class JWT:
