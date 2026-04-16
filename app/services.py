from sqlalchemy.orm import Session
from app.models import StudentGrade
from sqlalchemy import func


def get_students_by_faculty(db: Session, faculty: str):
    return db.query(StudentGrade).filter(StudentGrade.faculty == faculty).all()


def get_unique_subjects(db: Session):
    return db.query(StudentGrade.subject).distinct().all()


def get_students_low_score(db: Session, subject: str):
    return db.query(StudentGrade).filter(
        StudentGrade.subject == subject,
        StudentGrade.grade < 30
    ).all()


def get_avg_grade_by_faculty(db: Session, faculty: str):
    return db.query(func.avg(StudentGrade.grade)).filter(
        StudentGrade.faculty == faculty
    ).scalar()