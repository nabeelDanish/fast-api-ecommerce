import jwt

from passlib.context import CryptContext
from fastapi.exceptions import HTTPException
from fastapi import status
from dotenv import dotenv_values

from models import User


credentials = dotenv_values(".env")
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password):
    return password_context.hash(password)


async def verify_token(token: str):
    try:
        payload = jwt.decode(token, credentials["SECRET"], algorithms=["HS256"])
        user = await User.get(id_user=payload.get("id_user"))
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user
