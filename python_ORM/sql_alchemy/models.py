from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, Session, Relationship

CONNECTION_STRING = 'postgresql+psycopg2://postgres-user:password@172.18.0.2:5432/alchemy'

# connection with DB
engine = create_engine(CONNECTION_STRING)
# similar to models.Model in Django
Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    age = Column(Integer)
    city_id = Column(Integer, ForeignKey('cities.id'), default=1)
    city = Relationship('City', back_populates='employees')

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    employees = Relationship('Employee')


Base.metadata.create_all(engine)

