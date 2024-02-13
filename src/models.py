import datetime
from typing import Annotated
from sqlalchemy import Integer, String, Column, Table, MetaData, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
import enum
from src.database import str_256, Base

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
update_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.datetime.utcnow)]




class WorkersOrm(Base):
    __tablename__ = 'workers'

    id: Mapped[intpk]
    username: Mapped[str]


class Workload(enum.Enum):
    parttime = 'parttime'
    fulltime = 'fulltime'


class ResumeOrm(Base):
    __tablename__ = 'resume'

    id: Mapped[intpk]
    title: Mapped[str_256]
    compensation: Mapped[int | None]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    update_at: Mapped[update_at]


# metadata_obj = MetaData()
#
#
# workers_table = Table(
#     'workers',
#     metadata_obj,
#     Column('id', Integer, primary_key=True),
#     Column('username', String),
# )