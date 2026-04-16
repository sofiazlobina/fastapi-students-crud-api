from sqlalchemy import Column, Integer, String
from .database import Base


class StudentGrade(Base):
    __tablename__ = "student_grades"

    id = Column(Integer, primary_key=True, index=True)
    last_name = Column(String)
    first_name = Column(String)
    faculty = Column(String)
    subject = Column(String)
    grade = Column(Integer)