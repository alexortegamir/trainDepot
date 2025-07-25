from sqlalchemy import Column, Integer, String
from app.db import Base

class Locomotive(Base):
    __tablename__ = 'locomotives'
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    model = Column(String)
    era = Column(String)
    dcc_ready = Column(String)
    notes = Column(String)

class Wagon(Base):
    __tablename__ = 'wagons'
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    brand = Column(String)
    model = Column(String)
    era = Column(String)
    notes = Column(String)
