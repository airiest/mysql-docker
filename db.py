from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# sqlite
'''
DATABASE = 'sqlite:///db.sqlite3'
SQLITE3_NAME = "./db.sqlite3"
'''

# mysql
DATABASE = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8' % (
    "user",
    "password",
    "localhost:3306",
    "test_db",
)

ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=False
)

Base = declarative_base()
Session = sessionmaker(bind=ENGINE, autocommit=False, autoflush=False)
session = Session()
