from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv,find_dotenv
import os

load_dotenv(find_dotenv())
engine = create_engine(str(os.getenv("POSTGRES_URL")))
Session =  sessionmaker(bind=engine)

