from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, services, csv_loader, models

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/students")
def students(db: Session = Depends(get_db)):
    return crud.get_students(db)


@app.get("/faculty/{faculty}")
def by_faculty(faculty: str, db: Session = Depends(get_db)):
    return services.get_students_by_faculty(db, faculty)


@app.get("/subjects/unique")
def unique_subjects(db: Session = Depends(get_db)):
    return services.get_unique_subjects(db)


@app.get("/low-score/{subject}")
def low_score(subject: str, db: Session = Depends(get_db)):
    return services.get_students_low_score(db, subject)


@app.get("/avg/{faculty}")
def avg(faculty: str, db: Session = Depends(get_db)):
    return services.get_avg_grade_by_faculty(db, faculty)

@app.get("/export")
def export_csv(db: Session = Depends(get_db)):
    students = crud.get_students(db)

    with open("export.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Фамилия", "Имя", "Факультет", "Курс", "Оценка"])

        for s in students:
            writer.writerow([
                s.last_name,
                s.first_name,
                s.faculty,
                s.subject,
                s.grade
            ])

    return {"message": "export.csv created"}