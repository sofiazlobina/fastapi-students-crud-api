# FastAPI Students CRUD API

## Описание
CRUD API для работы с базой студентов + аналитика + импорт CSV.

---

## Функции

### CRUD
- Create student
- Read students
- Update grade
- Delete student

### Аналитика
- студенты по факультету
- уникальные курсы
- студенты с оценкой < 30
- средний балл по факультету

### CSV
- загрузка данных
- экспорт данных

---

## Запуск

```bash
uvicorn app.main:app --reload