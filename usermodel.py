from sqlalchemy import Table, Column , MetaData
from sqlalchemy.sql.sqltypes import Integer, String
from database import engine

meta = MetaData()

Users = Table('Users', meta,
    Column('id', String, unique=True, primary_key=True),
    Column('email', String),
    Column('password', String),
    Column('password_confirmation', String),
    Column('logged_in', String),
    Column('access_token', String)
)

meta.create_all(engine)
