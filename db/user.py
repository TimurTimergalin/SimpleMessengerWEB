from flask_login import UserMixin

from .db_session import SqlAlchemyBase
from sqlalchemy import Column as Cl
from sqlalchemy import orm, ForeignKey
import sqlalchemy as sql
from werkzeug.security import check_password_hash, generate_password_hash


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'
    id = Cl(sql.Integer, autoincrement=True, primary_key=True, nullable=False)
    login = Cl(sql.String(64), nullable=False, unique=True)
    username = Cl(sql.String(64), nullable=False, unique=True)
    password = Cl(sql.String(128), nullable=False)
    chats = orm.relationship('Chat', secondary='chat_to_user')

    def __init__(self, *args, **kwargs):
        SqlAlchemyBase.__init__(self, *args, **kwargs)
        self.password = generate_password_hash(self.password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, other_passport):
        return check_password_hash(self.password, other_passport)
