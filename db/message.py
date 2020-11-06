from .db_session import SqlAlchemyBase
from sqlalchemy import Column as Cl
from sqlalchemy import orm, ForeignKey
import sqlalchemy as sql


class Message(SqlAlchemyBase):
    __tablename__ = 'messages'
    id = Cl(sql.Integer, autoincrement=True, primary_key=True, nullable=False)
    text = Cl(sql.Text, nullable=False)
    author_id = Cl(sql.Integer, sql.ForeignKey('users.id', ondelete='CASCADE'))
    author = orm.relation('User')
    chat_id = Cl(sql.Integer, sql.ForeignKey('chats.id', ondelete='CASCADE'))
    chat = orm.relation('Chat')
