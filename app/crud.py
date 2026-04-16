from sqlalchemy.orm import Session
from app.models import StudentGrade


def create_student(db: Session, student):
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def get_students(db: Session):
    return db.query(StudentGrade).all()


def update_student_grade(db: Session, student_id: int, new_grade: int):
    student = db.query(StudentGrade).filter(StudentGrade.id == student_id).first()
    if student:
        student.grade = new_grade
        db.commit()
    return student


def delete_student(db: Session, student_id: int):
    student = db.query(StudentGrade).filter(StudentGrade.id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
    return student