from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "postgresql://stekkali:ydnas@localhost:5432/trello_app"

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()