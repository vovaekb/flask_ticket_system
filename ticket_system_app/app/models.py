import datetime
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.types import Date, Float, String, DateTime, UnicodeText
from sqlalchemy.orm import relationship, backref
from app import database 


class Employee(database.Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, index=True)
    place = Column(UnicodeText)
    manager_id = Column(Integer, ForeignKey('employee.id'))
    name = Column(UnicodeText)
    level = Column(Integer)
    information_tickets = relationship('InformationTicket', secondary='link')


class ActionTicket(database.Base):
    __tablename__ = 'action_ticket'
    id = Column(Integer, primary_key=True, index=True)
    frequency = Column(Integer, )
    author_id = Column(Integer)
    assignee_id = Column(Integer)
    date_format = "%Y-%m-%dT%H:%M:%S"
    creation_date = Column(DateTime,
                           server_default=datetime.datetime.now()
                           .strftime(date_format))
    until_date = Column(DateTime)
    completion_date = Column(DateTime, nullable=True)
    title = Column(UnicodeText)
    priority = Column(Integer)
    type = Column(Integer)
    text = Column(UnicodeText, nullable=True)
    tasks = relationship('Task', backref='action_ticket', lazy='dynamic')
    
    statuses_dict = {
        0: 'Assigned',
        1: 'In progress',
        2: 'Complete'
    }

    types_dict = {
        0: 'Regular',
        1: 'Irregular',
    }
    
    priorities_dict = {
        0: 'Low',
        1: 'Medium',
        2: 'High'
    }
    
    def status_string(self):
        return self.statuses_dict[self.status]
    
    def type_string(self):
        return self.types_dict[self.type]
    
    def priority_string(self):
        return self.priorities_dict[self.priority]

    @property
    def serialized(self):
        return {
            'id': self.id,
            'frequency': self.frequency,
            'author_id': self.author_id,
            'assignee_id': self.assignee_id,
            'creation_date': self.creation_date,
            'until_date': self.until_date,
            'completion_date': self.completion_date,
            'title': self.title,
            'priority': self.priority_string(),
            'type': self.type_string(),
            'text': self.text,
        }


class InformationTicket(database.Base):
    __tablename__ = 'information_ticket'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(UnicodeText) 
    status = Column(Integer, nullable=True)
    assignees = relationship('Employee', secondary='link')

    statuses_dict = {
        0: 'Accepted',
        1: 'Complete'
    }

    def status_string(self):
        return self.statuses_dict[self.status]
    
    def to_json(self):
        return {
            'id': self.id,
            'text': self.text,
            'status': self.status_string(),
        }


class Task(database.Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(UnicodeText)
    category = Column(UnicodeText)
    action_ticket_id = Column(Integer, ForeignKey('action_ticket.id'))
    
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'category': self.category,
            'action_ticket': self.action_ticket.title 
        }


class Link(database.Base):
   __tablename__ = 'link'
   information_ticket_id = Column(
       Integer, 
       ForeignKey('information_ticket.id'), 
       primary_key = True)

   employee_id = Column(
       Integer, 
       ForeignKey('employee.id'), 
       primary_key = True)

