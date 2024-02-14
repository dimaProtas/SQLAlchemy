from sqlalchemy import select, func, and_, Integer, cast
from database import async_session_factory, sync_session_factory, sync_engine, async_engine
from src.models import WorkersOrm, Base, ResumeOrm

class SyncOrm:
    @staticmethod
    def create_table():
        sync_engine.echo = False
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_workers_session_sync():
        with sync_session_factory() as session:
            paha = WorkersOrm(username='Paha')
            gleb = WorkersOrm(username='Gleb')
            session.add_all([paha, gleb])
            # flush отправляет запрос в базу данных
            # После flush каждый из работников получает первичный ключ id, который отдала БД
            session.flush()
            session.commit()

    @staticmethod
    def select_workers():
        with sync_session_factory() as session:
            query = select(WorkersOrm)
            res = session.execute(query)
            print(res.scalars().all())

    @staticmethod
    def update_worker(worker_id: int, new_username:str):
        with sync_session_factory() as session:
            current_username = session.get(WorkersOrm, worker_id)
            current_username.username = new_username
            # refresh нужен, если мы хотим заново подгрузить данные модели из базы.
            # Подходит, если мы давно получили модель и в это время
            # данные в базе данныхмогли быть изменены
            # session.refresh(current_username)

            # session.expire()
            # Отменяет действия обновления, и возвращает последние данные БД
            session.commit()

    @staticmethod
    def select_agv_compensation(like_languge: str):
        """
            select workload, avg(compensation)::int as avg_compensation
            from resumes
            where title like '%Python%' and compensation > 40000
            group by workload
            having avg(compensation) > 70000
        """
        with sync_session_factory() as session:
            query = select(
                ResumeOrm.workload,
                cast(func.avg(ResumeOrm.compensation), Integer).label("avg_compensation")
            ).select_from(ResumeOrm).filter(and_(
                ResumeOrm.title.contains(like_languge),
                ResumeOrm.compensation > 40000
            )).group_by(ResumeOrm.workload)
            print(query.compile(compile_kwargs={"literal_binds": True}))
            res = session.execute(query)
            result = res.all()
            print(result[0].avg_compensation)



class AsyncOrm:

    @staticmethod
    async def create_table():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def insert_workers_session_async():
        async with async_session_factory() as session:
            igor = WorkersOrm(username='Igor')
            vasya = WorkersOrm(username='Vasya')
            session.add(igor)
            session.add(vasya)
            await session.commit()

    @staticmethod
    async def select_workers():
        async with async_session_factory() as session:
            query = select(WorkersOrm)
            res = await session.execute(query)
            print(res.mappings().all())

    @staticmethod
    async def update_worker(worker_id: int, new_username: str):
        async with async_session_factory() as session:
            current_worker = await session.get(WorkersOrm, worker_id)
            current_worker.username = new_username
            await session.commit()
