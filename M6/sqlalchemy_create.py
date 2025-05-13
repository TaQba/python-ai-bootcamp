from sqlalchemy import Table, Column, Integer, String, MetaData, Float, Date, ForeignKey
from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db')

meta = MetaData()

stations = Table(
   'station',
   meta,
   Column('id', Integer, primary_key=True),
   Column('code', String),
   Column('name', String),
   Column('latitude', Float),
   Column('longitude', Float),
   Column('elevation', Float),
   Column('country', String),
   Column('state', String),
)
measures = Table(
   'measure',
   meta,
   Column('id', Integer, primary_key=True),
   Column('station_id', Integer, ForeignKey("station.id"), nullable=False),
   Column('date', Date),
   Column('precip', Float),
   Column('tobs', Integer)
)


def create_tables():
    meta.create_all(engine)
