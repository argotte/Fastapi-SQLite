from config.db import Base
from sqlalchemy import Column,Integer,String,Float


class Singer(Base):
    __tablename__="Singers"
    id=Column(Integer,primary_key=True,autoincrement=True)
    FirstName=Column(String,index=True)
    LastName=Column(String,index=True)