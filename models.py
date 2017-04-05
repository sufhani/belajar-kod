from sqlalchemy import Column, ForeignKey, Integer, String, Sequence, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Guide(Base):
    __tablename__ = 'guide'

    id = Column(Integer, Sequence('guide_id_seq'), primary_key=True)
    title = Column(String(130))
    text = Column(String)
    timestamp = Column(DateTime)

engine = create_engine('sqlite:///belajarkod.db')

Base.metadata.create_all(engine)