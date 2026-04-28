import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
TOKEN_EXPIRATION = int(
    os.getenv("TOKEN_EXPIRATION", 60)
)

DATABASE_URL = os.getenv("DATABASE_URL")