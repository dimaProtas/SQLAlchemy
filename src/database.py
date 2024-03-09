from sqlalchemy import String, create_engine, text
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from typing import Annotated
from config import settings

sync_engine = create_engine(
    url=settings.DATABASE_URL_pysycopg,
    echo=True, # логи
    pool_size=5, # количество подключений
    max_overflow=10, # Дополнительные подключения
)


async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True, # логи
    pool_size=5, # количество подключений
    max_overflow=10, # Дополнительные подключения
)


sync_session_factory = sessionmaker(sync_engine)
async_session_factory = async_sessionmaker(async_engine)


str_256 = Annotated[str, 256]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256)
    }

    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self):
        """Relationships не используются в repr(), т.к. могут вести к неожиданным подгрузкам"""
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__} {', '.join(cols)}>"

    # def __repr__(self):
    #     cols = []
    #     for col in self.__table__.columns.keys():
    #         cols.append(f"{col}={getattr(self, col)}")
    #     return f"<{self.__class__.__name__} {','.join(cols)}>" # Автоматически формерует ответ для логов

    # def __repr__(self):
    #     return f"<{self.__class__.name}>" # Можно переопределять __repr__ для классов моделей что бы получать красивый вывод в логах
    #
