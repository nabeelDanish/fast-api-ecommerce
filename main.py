from fastapi import FastAPI
from tortoise import models
from tortoise.contrib.fastapi import register_tortoise
from models import *
from authentication import *

# Signals
from tortoise.signals import post_save
from typing import List, Optional, Type
from tortoise import BaseDBAsyncClient

app = FastAPI()


@post_save(User)
async def create_business(
    sender: "Type[User]",
    instance: User,
    created: bool,
    using_db: "Optional[BaseDBAsyncClient]",
    using_fields: List[str],
):
    if created:
        business_obj = await Business.create(
            business_name=instance.username, owner=instance
        )

        await business_pydantic.from_tortoise_orm(business_obj)

        # Send the Email Function


@app.post("/registration")
async def user_registration(user: user_pydanticIn):
    user_info = user.dict(exclude_unset=True)
    user_info["password"] = get_hashed_password(user_info["password"])

    # Creating the user
    user_object = await User.create(**user_info)
    new_user = await user_pydantic.from_tortoise_orm(user_object)

    return {
        "status": "ok",
        "data": f"Hello {new_user.username}, thanks for choosing our service. Please check your email inbox and click on the link to confirm your registartion",
    }


@app.get("/")
def index():
    return {"message": "Hello! You have reached the index!"}


register_tortoise(
    app,
    db_url="sqlite://database.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
