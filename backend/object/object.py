from datetime import datetime

from flask_login import UserMixin
from mongoengine import Document, StringField, IntField, DateTimeField
from pydantic import BaseModel, EmailStr


class UserModel(BaseModel, UserMixin):
    id: str = None
    username: str
    password: str
    email: EmailStr

    def get_id(self):
        return self.id

    class Config:
        orm_mode = True


class User(Document):
    id = StringField(required=True)
    username = StringField(required=True)
    password = StringField(required=True)
    email = StringField(required=True)

    def to_model(self):
        return UserModel.from_orm(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


class ProblemModel(BaseModel):
    id: str
    title: str
    likes: int
    contributor: str
    content: str
    pass_num: int
    submit_num: int


class Problem(Document):
    id = StringField(required=True)
    title = StringField(required=True)
    likes = IntField(required=False)
    contributor = StringField(required=True)
    content = StringField(required=True)
    pass_num = IntField(required=False)
    submit_num = IntField(required=False)


class SubmitModel(BaseModel):
    id: str
    userid: str
    time: datetime
    status: str
    content: str


class Submit(Document):
    id = StringField(required=True)
    userid = StringField(required=True)
    time = DateTimeField(required=True)
    status = StringField(required=True)
    content = StringField(required=True)
