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
class Shelfs(Bace):
    __tablename__="shelfs"
    id=Column(Integer,primary_key=True)
    name=Column(String(128))
    date=Column(DateTime,default=datetime.now())
    def __init__(self,name,date) -> None:
        self.name=name
        self.date=date

class Traces(Bace):
    __tablename__="traces"
    id=Column(Integer,primary_key=True)
    book_id=Column(Integer)
    shelf_id=Column(Integer)
    date=Column(DateTime,default=datetime.now())
    def __init__(self,book_id,shelf_id,date) -> None:
        self.book_id=book_id
        self.shelf_id=shelf_id
        self.date=date
    

