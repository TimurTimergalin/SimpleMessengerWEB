from .db_session import SqlAlchemyBase
from sqlalchemy import Column as Cl
from sqlalchemy import orm, ForeignKey
import sqlalchemy as sql


class ChatToUser(SqlAlchemyBase):
    __tablename__ = 'chat_to_user'
    id = Cl(sql.Integer, autoincrement=True, primary_key=True, nullable=False)
    user_id = Cl(sql.Integer, sql.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    chat_id = Cl(sql.Integer, sql.ForeignKey('chats.id', ondelete='CASCADE'), nullable=False)
