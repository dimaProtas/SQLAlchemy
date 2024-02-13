from sqlalchemy import Integer, String, Column, Table, MetaData

metadata_obj = MetaData()


workers_table = Table(
    'workers',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('username', String),
)