## Описание проекта
Проект представляет собой REST API для управления данными студентов с использованием FastAPI, SQLAlchemy и JWT-аутентификации.

### Сервис позволяет:
- управлять студентами (CRUD операции);
- загружать данные из CSV-файла;
- фильтровать и анализировать данные;
- работать только авторизованным пользователям.

### Технологии
- Python 3.11+
- FastAPI
- SQLAlchemy
- Alembic
- SQLite
- JWT (python-jose)
- Passlib (bcrypt)
- Uvicorn

### Запуск проекта
1. Установка зависимостей
``` pip install -r requirements.txt ```

2. Запуск сервера
```cuvicorn app.main:app --reload ```

3. Swagger документация
``` http://127.0.0.1:8000/docs ```

### Авторизация

1. Регистрация
```
POST /auth/register
{
  "username": "test",
  "password": "test123"
}
```

2. Логин

```
POST /auth/login
{
  "username": "test",
  "password": "test123"
}
```

3. Ответ:

```
{
  "access_token": "token",
  "token_type": "bearer"
}
```