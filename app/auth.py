from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext


SECREAT_KEY = "Trello_APP"
ALGORITHM = "HS256"
TOKEN_EXPIRATION = 60

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password : str):
    return pwd_context.hash(password)

def create_access_token(data : dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=TOKEN_EXPIRATION
    )

    to_encode.update({'exp':expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECREAT_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

def verify_password(plain_password : str,hashed_password : str):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )