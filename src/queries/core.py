import asyncio
from sqlalchemy import text, insert
from database import sync_engine, async_engine
from models import metadata_obj, workers_table


def func_sync():
    with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT 1, 2, 3 union select 4, 5, 6"))
        print(f"{res.all()=}")


# Асинхронный контекст менаджер и движок
async def func_async():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT 1, 2, 3 union select 4, 5, 6"))
        print(f"{res.all()=}")


# asyncio.run(func_async()) # вызвать асинхронную функцию
# func_sync() # вызвать синхронную функцию


def create_table():
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)


# Асинхронная операция insert
async def insert_workers_async():
    async with async_engine.connect() as conn:
        stmt = ("""INSERT INTO workers (username) VALUES ('Bobr'), ('Volk');""")
        await conn.execute(text(stmt))
        await conn.commit()


# Синхронная операция insert
def inser_workers_sync():
    with sync_engine.connect() as conn:
        stmt = insert(workers_table).values(
            [
                {'username': 'Dima'},
                {'username': 'Ira'},
            ]
        )
        conn.execute(stmt)
        conn.commit()

