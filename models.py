from datetime import datetime
import hashlib

from db import Base

from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN


class User(Base):
    '''
    id       : 主キー
    username : ユーザー名
    password : パスワード
    mail     : メールアドレス
    '''
    __tablename__ = 'user'
    id = Column(
        'id',
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True
    )
    username = Column(
        'username',
        String(256)
    )
    password = Column(
        'password',
        String(256)
    )
    mail = Column(
        'mail',
        String(256)
    )

    def __init__(self, username: str, password: str, mail: str):
        self.username = username
        self.password = hashlib.md5(password.encode()).hexdigest()
        self.mail = mail

    def __str__(self):
        return str(self.id) + \
            ': username = ' + str(self.username) + \
            ', password = ' + self.password + \
            ', mail = ' + self.mail


class Task(Base):
    '''
    id       : 主キー
    user_id  : 作成者（外部キー）
    date     : 作成日
    content  : 内容
    deadline : 締め切り
    done     : タスクを終了フラグ
    '''
    __tablename__ = 'task'
    id = Column(
        'id',
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True
    )
    user_id = Column(
        'user_id',
        ForeignKey('user.id')
    )
    date = Column(
        'date',
        DateTime,
        default=datetime.now(),
        nullable=False,
        server_default=current_timestamp()
    )
    content = Column(
        'content',
        String(256)
    )
    deadline = Column(
        'deadline',
        DateTime,
        default=None,
        nullable=False
    )
    done = Column(
        'done',
        BOOLEAN,
        default=False,
        nullable=False
    )

    def __init__(self, user_id: int, content: str, deadline: datetime):
        self.user_id = user_id
        self.date = datetime.now()
        self.content = content
        self.deadline = deadline
        self.done = False

    def __str__(self):
        return str(self.id) + \
            ': user_id = ' + str(self.user_id) + \
            ', date = ' + self.date.strftime('%Y/%m/%d %H:%M:%S') + \
            ', content = ' + self.content + \
            ', deadline = ' + self.deadline.strftime('%Y/%m/%d %H:%M:%S') + \
            ', done = ' + str(self.done)
