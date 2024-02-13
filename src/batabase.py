import asyncio

from sqlalchemy import String, create_engine, text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from src.config import settings

# engine = create_engine(
#     url=settings.DATABASE_URL_pysycopg,
#     echo=True, # логи
#     pool_size=5, # количество подключений
#     max_overflow=10, # Дополнительные подключения
# )


# with engine.connect() as conn:
#     res = conn.execute(text("SELECT 1, 2, 3 union select 4, 5, 6"))
#     print(f"{res.all()=}")


async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True, # логи
    pool_size=5, # количество подключений
    max_overflow=10, # Дополнительные подключения
)

# Асинхронный контекст менаджер и движок
async def func():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT 1, 2, 3 union select 4, 5, 6"))
        print(f"{res.all()=}")


asyncio.run(func()) # вызвать асинхронную функцию