# import os
# import sys
# sys.path.insert(1, os.path.join(sys.path[0], '..'))
import asyncio

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
SyncOrm.select_workers_with_condition_relationship()

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
    #
    # await AsyncOrm.create_table()
    # await AsyncOrm.insert_workers_session_async()
    # await AsyncOrm.select_workers()
    # await AsyncOrm.update_worker(1, 'Harek')


# if __name__ == "__main__":
#     asyncio.run(main())

