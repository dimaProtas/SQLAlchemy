import datetime
from typing import Annotated, Optional
from sqlalchemy import Integer, String, Column, Table, MetaData, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
import enum
from database import str_256, Base

from sqlalchemy import (
    TIMESTAMP,
    CheckConstraint,
    Column,
    Enum,
    ForeignKey,
    Index,
    Integer,
    MetaData,
    PrimaryKeyConstraint,
    String,
    Table,
    text,
)

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.datetime.utcnow)]




class WorkersOrm(Base):
    __tablename__ = 'workers'

    id: Mapped[intpk]
    username: Mapped[str]

    resume: Mapped[list["ResumeOrm"]] = relationship(
        back_populates="worker", # Избегает предупреждений в SQLAlchemy
        # backref="worker" # Устарело не рекомендуеться использовать
    )

    resume_parttime: Mapped[list["ResumeOrm"]] = relationship(
        back_populates="worker",
        primaryjoin="and_(WorkersOrm.id == ResumeOrm.worker_id, ResumeOrm.workload == 'parttime')",
        order_by="ResumeOrm.id.desc()", # Сортировка ещё может быть asc()
    )


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
    updated_at: Mapped[updated_at]

    worker: Mapped["WorkersOrm"] = relationship(
        back_populates="resume", # Избегает предупреждений в SQLAlchemy
    )

    # def __repr__(self):
    #     return f"Resume id={self.id}, title={self.title}" # Пример переобределения

    vacancies_replied: Mapped[list["VacanciesOrm"]] = relationship(
        back_populates="resumes_replied",
        secondary="vacancies_replies", # так же нужно указывать для связи many_to_many
    ) # Для связи many_to_many

    repr_cols_num = 2
    repr_cols = ("created_at", )

    __table_args__ = (
        Index("title_index", "title"),
        CheckConstraint("compensation > 0", name="checl_compensation_positive"),
    )


class VacanciesOrm(Base):
    __tablename__ = "vacancies"

    id: Mapped[intpk]
    title: Mapped[str_256]
    compensation: Mapped[Optional[int]]

    resumes_replied: Mapped[list["ResumeOrm"]] = relationship(
        back_populates="vacancies_replied",
        secondary="vacancies_replies",
    )


# Таблица для связи many_to_many
class VacanciesRepliesOrm(Base):
    __tablename__ = "vacancies_replies"

    resume_id: Mapped[int] = mapped_column(
        ForeignKey("resume.id", ondelete="CASCADE"),
        primary_key=True,
    )
    vacancy_id: Mapped[int] = mapped_column(
        ForeignKey("vacancies.id", ondelete="CASCADE"),
        primary_key=True,
    )

    cover_letter: Mapped[Optional[str]]


metadata_obj = MetaData()


workers_table = Table(
    'workers',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('username', String),
)

resumes_table = Table(
    "resumes",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("title", String(256)),
    Column("compensation", Integer, nullable=True),
    Column("workload", Enum(Workload)),
    Column("worker_id", ForeignKey("workers.id", ondelete="CASCADE")),
    Column("created_at", TIMESTAMP,server_default=text("TIMEZONE('utc', now())")),
    Column("updated_at", TIMESTAMP,server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.datetime.utcnow),
)

vacancies_table = Table(
    "vacancies",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("compensation", Integer, nullable=True),
)

vacancies_replies_table = Table(
    "vacancies_replies",
    metadata_obj,
    Column("resume_id", ForeignKey("resumes.id", ondelete="CASCADE"), primary_key=True),
    Column("vacancy_id", ForeignKey("vacancies.id", ondelete="CASCADE"), primary_key=True),
)