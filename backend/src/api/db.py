import os
import sqlmodel
from sqlmodel import Session, SQLModel
import time
from sqlalchemy.exc import OperationalError

DATABSE_URL = os.environ.get("DATABASE_URL")

if not DATABSE_URL:
    raise NotImplementedError("DATABASE_URL is not set in environment variables.")


engine = sqlmodel.create_engine(DATABSE_URL) # connection factory


#database model
def init_db():
    retries = 5
    while retries > 0:
        try:
            SQLModel.metadata.create_all(engine) # table creation
            print("Database tables created!")
            break
        except OperationalError:
            retries -= 1
            print("DB not ready, retrying in 2s...")
            time.sleep(2)
    else:
        raise Exception("Could not connect to DB after several attempts")

# api route
def get_session():
    with Session(engine) as session:
        yield session