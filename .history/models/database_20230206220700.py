from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

database_file=os.path.join(os.path.abspath(os.path.dirname(__file__)),"bookl.db")
en=create_engine("sqlite://?"+database_file,convert_unicode=True,echo=True)

