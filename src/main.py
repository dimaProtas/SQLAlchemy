# import os
# import sys
# sys.path.insert(1, os.path.join(sys.path[0], '..'))
import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# from queries.core import SyncCore, AsyncCore
from queries.orm import SyncOrm, AsyncOrm

# SyncOrm.create_table()
# SyncOrm.insert_workers_session_sync()
# SyncOrm.select_workers()
# SyncOrm.update_worker(1, 'Gus')
# SyncOrm.select_agv_compensation('Python')
# SyncOrm.insert_addworkers_addresume()
# SyncOrm.join_cte_subquery_window_func()
# SyncOrm.select_workers_with_lazy_relationship()
# SyncOrm.select_workers_with_joined_relationship()
# SyncOrm.select_workers_with_selectin_relationship()
# SyncOrm.select_workers_with_condition_relationship()

# SyncCore.create_table()
# SyncCore.inser_workers_sync()
# SyncCore.select_users()
# SyncCore.update_worker_sql_query(2, 'Lox')
# SyncCore.update_worker_query_sqlalchemy(1, 'Good name')




# async def main():
    # await AsyncCore.create_tables()
    # await AsyncCore.insert_workers_async()
    # await AsyncCore.select_users()
    # await AsyncCore.update_workers(1, 'Cool boy')

    # await AsyncOrm.create_table()
    # await AsyncOrm.insert_workers_session_async()
    # await AsyncOrm.select_workers()
    # await AsyncOrm.update_worker(1, 'Harek')

def create_fastapi_app():
    app = FastAPI(title="FastaAPI")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
    )

    @app.get("/workers", tags=["Кандидат"])
    async def get_workers():
        workers = await AsyncOrm.convert_workers_to_dto()
        return workers

    @app.get("/resumes", tags=["Ресюме"])
    async def get_resumes():
        resumes = await AsyncOrm.select_resumes_with_all_relationships()
        return resumes

    @app.get("/workers_api", tags=["Кондидаты API"])
    async def get_workers_api():
        workers = await AsyncOrm.select_workers_fastapi()
        return workers

    return app

app = create_fastapi_app()


if __name__ == "__main__":
    # asyncio.run(main())
    uvicorn.run(
        app="main:app",
        reload=True,
    )
