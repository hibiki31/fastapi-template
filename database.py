from starlette.requests import Request
from databases import Database
from sqlalchemy import MetaData, create_engine

DATABASE_URL = 'sqlite:///database.sqlite3'

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(DATABASE_URL, echo=True)

def get_connection(request: Request):
    return request.state.connection