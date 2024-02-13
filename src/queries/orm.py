from database import async_session_factory, sync_session_factory, sync_engine
from src.models import WorkersOrm, Base


def create_table():
    print(Base.metadata)
    Base.metadata.drop_all(sync_engine)
    sync_engine.echo = True
    Base.metadata.create_all(sync_engine)
    sync_engine.echo = True


def insert_workers_session_sync():
    with sync_session_factory() as session:
        paha = WorkersOrm(username='Paha')
        gleb = WorkersOrm(username='Gleb')
        session.add_all([paha, gleb])
        session.commit()


async def insert_workers_session_async():
    async with async_session_factory() as session:
        igor = WorkersOrm(username='Igor')
        vasya = WorkersOrm(username='Vasya')
        session.add(igor)
        session.add(vasya)
        await session.commit()
