from sqlalchemy import Column, Integer, Float, String, create_engine # used for setting up an SQLite database, defining the table, and inserting data
from sqlalchemy.orm import sessionmaker, declarative_base

# a declarative base for our model to inherit from
Base = declarative_base()

class WeatherDatabase(Base):
    __tablename__ = 'WeatherRecords'

# defines the columns for the 'WeatherRecords' table
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    month = Column(String, nullable=False)
    day = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    avg_temp_5yr = Column(Float)
    min_temp_5yr = Column(Float)
    max_temp_5yr = Column(Float)
    avg_wind_speed_5yr = Column(Float)
    min_wind_speed_5yr = Column(Float)
    max_wind_speed_5yr = Column(Float)
    sum_rain_5yr = Column(Float)
    min_rain_5yr = Column(Float)
    max_rain_5yr = Column(Float)

# creates the SQLite db engine and binds it to the weather_data.db file
engine = create_engine('sqlite:///weather_data.db', echo=True)

# creates the table defined by the "Base" subclass, which is WeatherDatabase
Base.metadata.create_all(engine)

# creates a 'sessionmaker', a factory function that makes new Session objects which allow you to interact w/ the database
Session = sessionmaker(bind=engine)

#creates a session instance, allowing you to query/modify the database
session = Session()