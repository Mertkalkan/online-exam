from sqlalchemy import Column, String

from .entity import Entity, Base

class Exam(Entity, Base):
    __tablename__ = 'exams'

    title = Column(String(16))
    description = Column(String(64))

    def __init__(self, title, description, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description