from flask import Flask
from flask_login import LoginManager
from config import Config

from db.db_session import create_session, global_init
from db.user import User
from db.chat_to_user import ChatToUser
from db.chat import Chat
from db.message import Message
from funcs import *

app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager(app)

