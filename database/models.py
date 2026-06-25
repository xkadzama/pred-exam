from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class CarDealer(Base):
	__tablename__ = 'car_dealers'

	id = Column(Integer, primary_key=True)
	name = Column(String, unique=True, nullable=False)
	city = Column(String, nullable=True)
	address = Column(String, nullable=True)
	owner = Column(String, nullable=True)


class Car(Base):
	__tablename__ = 'cars'

	id = Column(Integer, primary_key=True)
	brand = Column(String, nullable=False)
	model = Column(String, nullable=False)
	year = Column(String, nullable=True)
	price = Column(Float, nullable=False)
	dealer_id = Column(Integer, ForeignKey('car_dealers.id', ondelete='CASCADE'), nullable=False)
