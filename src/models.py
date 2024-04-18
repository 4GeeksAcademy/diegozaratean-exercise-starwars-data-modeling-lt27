import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teacher'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    city = Column(String(250))    
    age = Column(Integer)


class Course(Base):
    __tablename__ = 'course'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))   
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    teacher = relationship(Teacher) 


class Student(Base):
    __tablename__ = 'student'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    city = Column(String(250))    
    level = Column(String(250))  

class StudentCourse(Base):
    __tablename__ = 'student_course'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    student = relationship(Student)
    student_id = Column(Integer, ForeignKey('student.id'))
    course_id = Column(Integer, ForeignKey('course.id'))
    course = relationship(Course)
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
