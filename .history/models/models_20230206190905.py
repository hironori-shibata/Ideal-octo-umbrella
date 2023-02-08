from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime
class Books(Base):
    __tablename__="books"
    id=Column(Integer,primary_key=True)
    title=Column(String(128))
    author=Column(String(128))
    date=Column(DateTime,default=datetime.now())
    def __init__(self,title=None,author=None,date=None) -> None:
        self.title=title
        self.author=author
        self.date=date
        #super().__init__()