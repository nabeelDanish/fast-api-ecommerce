from fastapi import (
    BackgroundTasks,
    UploadFile,
    File,
    Form,
    Depends,
    HTTPException,
    status,
)
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

config = ConnectionConfig(
    MAIL_USERNAME="",
    MAIL_PASSWORD="",
    MAIL_FROM="",
    MAIL_PORT=587,
    MAIL_SERVER="smpt.gmail.com",
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
)
