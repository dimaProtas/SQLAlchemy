SQLAlchemy:

branch_1
- Настройки подключения к БД
- Асинхроное подключение
- Синхронное подключение
- pydantic_settings и валидация .env переменных

branch_2
- Создание таблицы в императивном стиле
- Создание таблиц в БД через create_all()
- Удаление всех таблиц из БД drop_all()
- Асинхронная и синхронная вставка данных в таблицу
- Вставка данных через сырые запросы
- Вставка данных через сырые запросы

branch_3
- Обьявление таблицы в декларативном стиле
- метаданные при таком обьвлении храняться в DeclarativeBase
- Использование sessionmaker и async_sessionmaker для взаимодейстаия с БД

branch_4
- Обьявление таблиц в декларативном стиле
- Использование Annotated для типизации данных
- Нужно импортировать Base из models.py

branch_5
- session.flush() пример использования
- session.refresh() пример использования
-  session.expire() пример использования
- ORM запросы (избегать SQL инъекций)
- SQLAlchemy Core запросы 

branch_6
-  как SQL запросы переносить на язык Алхимии
- используем func, cast, label и другие функции SQLAlchemy

branch_7
- как SQL запросы переносить на язык Алхимии
- используем CTE
- используем subquery
- используем aliased

branch_8
- Введение в RELATIONSHIP
- joinedload - для 'many to one' и для 'one to one' (многие ко многим и один к одному)
- selectinload - для 'one to many' и 'many to many' (один ко многим, многие ко многим)
- __repr__ для красивова вывода в логи (несколько вариантов)

branch_9 
- Продвинутый RELATIONSHIP

branch_10
- Pydantic DTO
- FastAPI + SQLAlchemy