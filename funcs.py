from db.user import User
from db.chat_to_user import ChatToUser
from db.chat import Chat
from db.message import Message
from sqlalchemy.orm import Session


def register_user(session: Session, **kwargs):
    kwargs['id'] = None  # Задётся автоинкрементом
    check_email = session.query(User).filter(User.login == kwargs['login']).first()
    if check_email:
        return 'Этот адрес почты уже используется'
    check_username = session.query(User).filter(User.username == kwargs['username']).first()
    if check_username:
        return 'Это имя уже занято'
    user = User(**kwargs)
    session.add(user)
    session.commit()
    return user
