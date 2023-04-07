import json
import re
from datetime import datetime

from flask_login import UserMixin
from pydantic import BaseModel, Field, validator

from converter import sql_datetime_to_datetime
from database import sql
from extentions import bcrypt


class User(UserMixin, sql.Model):
    __tablename__ = 'user'
    id = sql.Column(
        sql.Integer,
        primary_key=True
    )
    username = sql.Column(
        sql.String(100),
        unique=True
    )
    nickname = sql.Column(
        sql.String(100)
    )
    password = sql.Column(
        sql.String(500)
    )
    email = sql.Column(
        sql.String(100)
    )
    level = sql.Column(
        sql.Integer
    )
    create_time = sql.Column(
        sql.DateTime
    )

    def __init__(self, password, **kwargs):
        super(User, self).__init__(**kwargs)
        self.set_password(password)

    def __repr__(self):
        return '<User %s: %s@%s>' % (self.username, self.nickname, self.level)

    def set_password(self, password):
        _hash = bcrypt.generate_password_hash(password, method='sha256').decode('utf-8')
        self.password = _hash

    def to_json(self):
        return {
            "user": {
                "id": self.id,
                "username": self.username,
                "nickname": self.nickname,
                "email": self.email,
                "level": self.level,
                "create_time": sql_datetime_to_datetime(self.create_time).isoformat()
            }
        }


class UserModel(BaseModel):
    username: str = Field(regex=r'^[a-zA-Z0-9_-]{3,16}$')
    nickname: str = Field(regex=r'^[a-zA-Z0-9_-]{3,16}$')
    password: str
    email: str = Field(regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    level: int
    create_time: datetime

    @validator('username')
    def username_validator(cls, name):
        if not re.match(r'^[a-zA-Z0-9_-]{3,16}$', name):
            raise ValueError("invalid email format")
        return name

    @validator('nickname')
    def nickname_validator(cls, name):
        if not re.match(r'^[a-zA-Z0-9_-]{3,16}$', name):
            raise ValueError("invalid email format")
        return name

    @validator('password')
    def password_validator(cls, passwd):
        if len(passwd) < 8 or len(passwd) > 16:
            raise ValueError("invalid password length")
        return passwd

    @validator('email')
    def email_validator(cls, email):
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            raise ValueError("invalid email format")
        return email


class TestModel(BaseModel):
    username: str = Field(..., regex=r'^[a-zA-Z0-9_-]{3,16}$')
    password: str
    size: int = Field(..., ge=0, le=100)
    time: datetime

    @validator('username')
    def test_validator(cls, name):
        if not re.match(r'^[a-zA-Z0-9_-]{3,16}$', name):
            raise ValueError("invalid email format")
        return name


if __name__ == '__main__':
    user_input = {"username": "t1234", "nickname": "test", "password": "*^%&^$^&#", "size": 10,
                  "time": "1970-01-01T23:59:59"}
    user = TestModel(**user_input)
    print(user.__dict__)
