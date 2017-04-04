from sqlalchemy import Column, ForeignKey, Integer, String, Sequence, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Guide(Base):
    __tablename__ = 'guide'

    id = Column(Integer, Sequence('guide_id_seq'), primary_key=True)
    title = Column(String(50))
    text = Column(String)
    created_at = Column(DateTime)