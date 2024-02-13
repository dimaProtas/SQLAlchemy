# import os
# import sys
# sys.path.insert(1, os.path.join(sys.path[0], '..'))
import asyncio

# from queries.core import create_table, insert_workers_async, inser_workers_sync
from queries.orm import create_table, insert_workers_session_sync, insert_workers_session_async


create_table()
# inser_workers_sync()
# asyncio.run(insert_workers_async())

# insert_workers_session_sync()
# asyncio.run(insert_workers_session_async())
