from sqlalchemy import Column, String
from .entity import Entity, Base
from marshmallow import Schema, fields




class Exam(Entity, Base):
    __tablename__ = 'exams'

    title = Column(String(16))
    description = Column(String(64))

    def __init__(self, title, description, created_by):
        Entity.__init__(self, created_by)
        self.title = title
        self.description = description

# Here, you are defining a class called Exam that inherits from Entity and from Base. 
# This entity contains, besides the properties defined by its superclasses, two properties: title and description. Besides that, 
# this class also defines that instances of it must be persisted to and retrieved from a table called exams


class ExamSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    description = fields.Str()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    last_updated_by = fields.Str()   

# In the new version of this file, you are using the Schema 
# class of marshmallow to define a 
# new class called ExamSchema. You will use this class 
# to transform instances of Exam into JSON objects.