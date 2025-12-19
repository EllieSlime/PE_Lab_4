# PE_Lab_4 — FastAPI проект для управления студентами и группами

## Описание проекта

Проект представляет собой REST API для работы со студентами и группами.
С его помощью можно:

* Создавать и удалять студентов и группы
* Получать информацию о студентах и группах
* Получать список всех студентов и групп
* Добавлять студента в группу и удалять из группы
* Переводить студента из одной группы в другую
* Получать список студентов в конкретной группе

Проект разработан с использованием **FastAPI**, **SQLAlchemy** и **PostgreSQL**.
Архитектура соблюдает принципы **SOLID, DRY, KISS**, слои разделены на:

* `api` — HTTP слой и роуты
* `services` — бизнес-логика
* `repositories` — доступ к базе данных
* `schemas` — Pydantic-схемы (DTO)
* `db` — модели и сессии базы данных
* `core` — конфигурация

Все данные хранятся в PostgreSQL, развёрнутой в Docker-контейнере.

---

## Структура проекта

```
PE_Lab_4
│
├── app
│   ├── main.py
│   ├── api
│   ├── core
│   ├── db
│   ├── schemas
│   ├── services
│   └── repositories
│
├── .env.example
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Переменные окружения

Для конфигурации проекта используется `.env` файл.
Пример содержимого `.env.example`:

```env
POSTGRES_DB=students_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

DATABASE_URL=postgresql://postgres:postgres@db:5432/students_db
```

Перед запуском создайте файл `.env` на основе `.env.example`.

---

## Docker

Для удобного запуска проекта используется **docker-compose**.

### docker-compose.yml

* Сервис `db` — PostgreSQL
* Сервис `api` — FastAPI, подключается к базе и слушает порт 8000

---

## Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone <repository-url>
cd PE_Lab_4
```

2. Создайте `.env` на основе примера:

```powershell
copy .env.example .env
```

3. Запустите проект через Docker:

```powershell
docker-compose up --build
```

4. Доступ к API:

* API: [http://localhost:8000](http://localhost:8000)
* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Эндпоинты API

| Действие                           | Метод  | URL                                            |
| ---------------------------------- | ------ | ---------------------------------------------- |
| Создать студента                   | POST   | `/students/`                                   |
| Создать группу                     | POST   | `/groups/`                                     |
| Получить студента по id            | GET    | `/students/{id}`                               |
| Получить группу по id              | GET    | `/groups/{id}`                                 |
| Удалить студента                   | DELETE | `/students/{id}`                               |
| Удалить группу                     | DELETE | `/groups/{id}`                                 |
| Получить список студентов          | GET    | `/students/`                                   |
| Получить список групп              | GET    | `/groups/`                                     |
| Добавить студента в группу         | POST   | `/students/{id}/add_to_group/{group_id}`       |
| Удалить студента из группы         | POST   | `/students/{id}/remove_from_group`             |
| Получить студентов в группе        | GET    | `/groups/{id}/students`                        |
| Перевести студента в другую группу | POST   | `/students/{id}/transfer_group/{new_group_id}` |

---

## Технологии

* Python 3.11
* FastAPI
* SQLAlchemy
* PostgreSQL
* Docker / docker-compose
* Pydantic

---

## Архитектура

Проект разделён на слои для чистоты кода и удобства поддержки:

* **API** — маршруты и HTTP-эндпоинты
* **Services** — бизнес-логика, операции с группами и студентами
* **Repositories** — доступ к базе данных, CRUD-операции
* **Schemas** — Pydantic-схемы для валидации данных
* **DB** — SQLAlchemy-модели и сессии
* **Core** — конфигурация проекта и переменные окружения


