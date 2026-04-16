import csv
from app.models import StudentGrade


def load_csv(file_path: str):
    students = []

    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append(
                StudentGrade(
                    last_name=row["Фамилия"],
                    first_name=row["Имя"],
                    faculty=row["Факультет"],
                    subject=row["Курс"],
                    grade=int(row["Оценка"])
                )
            )

    return students