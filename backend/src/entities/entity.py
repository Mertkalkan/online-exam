from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db_url = 'localhost:3306'
db_name = 'online_exam'
db_user = 'root'
db_password = ''
engine = create_engine('mysql+pymysql://root@localhost:3306/online_exam')


Session = sessionmaker(bind=engine)

Base = declarative_base()

class Entity():
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_updated_by = Column(String(16))

    def __init__(self, created_by):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.last_updated_by = created_by




#  You will use this class as the superclass to all your 
#  entities. This will be useful to avoid having to repeat some boilerplate code to connect to
#  the database and to define some common properties