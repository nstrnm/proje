from sqlalchemy import Boolean, Column, Integer, String
from .database import Base

class course(Base):

    __tablename__ = "course"

    cid = Column(String , primary_key=True)
    cname = Column(String)
    department = Column(String)
    credit = Column(Integer)

class student(Base):

    __tablename__ = "student"

    stid = Column(String , primary_key=True)
    fname = Column(String)
    lname = Column(String)
    father = Column(String)
    birth = Column(Integer)
    ids = Column(Integer)
    borncity = Column(String)
    address = Column(String)
    postalcode = Column(Integer)
    cphone = Column(Integer)
    hphone = Column(Integer)
    department = Column(String)
    major = Column(String)
    married = Column(Boolean)
    id = Column(Integer)
    cid = Column(Integer)
    lids = Column(Integer)

class lecturer(Base):

    __tablename__ = "lecturer"

    lid = Column(String , primary_key=True)
    fname = Column(String)
    lname= Column(String)
    id = Column(Integer)
    department = Column(String)
    major = Column(String)
    birth = Column(Integer)
    borncity = Column(String)
    address = Column(String)
    postalcode = Column(Integer)
    cphone = Column(Integer)
    hphone = Column(Integer)
    cid = Column(Integer)