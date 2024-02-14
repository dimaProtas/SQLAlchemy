import asyncio
from sqlalchemy import text, insert, select, update
from database import sync_engine, async_engine
from models import metadata_obj, workers_table, Base, WorkersOrm



class SyncCore:
    @staticmethod
    def create_table():
        sync_engine.echo = False
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True


    # Синхронная операция insert
    @staticmethod
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

    @staticmethod
    def select_users():
        with sync_engine.connect() as conn:
            query = select(WorkersOrm)
            res = conn.execute(query)
            print(res.all())

    @staticmethod
    def update_worker_sql_query(worker_id: int, new_username: str):
        with sync_engine.connect() as conn:
            stmt = text("UPDATE workers SET username=:new_username WHERE id=:worker_id")
            stmt = stmt.bindparams(new_username=new_username, worker_id=worker_id)
            conn.execute(stmt)
            conn.commit()


    def update_worker_query_sqlalchemy(worker_id: int, new_username: str):
        with sync_engine.connect() as conn:
            stmt = update(WorkersOrm).values(username=new_username).filter_by(id=worker_id) # Фильтрация через метод filter_by
            # stmt = update(WorkersOrm).values(username=new_username).where(WorkersOrm.id==worker_id) # Фильтрация через метод where
            conn.execute(stmt)
            conn.commit()


class AsyncCore:

    @staticmethod
    async def create_tables():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    # Асинхронная операция insert
    @staticmethod
    async def insert_workers_async():
        async with async_engine.connect() as conn:
            stmt = ("""INSERT INTO workers (username) VALUES ('Bobr'), ('Volk');""")
            await conn.execute(text(stmt))
            await conn.commit()

    @staticmethod
    async def select_users():
        async with async_engine.connect() as conn:
            query = select(WorkersOrm)
            res = await conn.execute(query)
            print(res.all())

    @staticmethod
    async def update_workers(worker_id: int, new_username:str):
        async with async_engine.connect() as conn:
            stmt = update(WorkersOrm).values(username=new_username).filter_by(id=worker_id)
            await conn.execute(stmt)
            await conn.commit()
