from .db_session import SqlAlchemyBase
from sqlalchemy import Column as Cl
from sqlalchemy import orm, ForeignKey
import sqlalchemy as sql


class Chat(SqlAlchemyBase):
    __tablename__ = 'chats'
    id = Cl(sql.Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Cl(sql.String(64), nullable=False)
    users = orm.relationship('User', secondary='chat_to_user')
    messages = orm.relation('Message', back_populates='chat')
