from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost:8000/Autonomous-BI-DWH")
Session = sessionmaker(engine)
Base = declarative_base()

dwh = Session()