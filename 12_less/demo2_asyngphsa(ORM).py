from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table, Column, Integer, String, Date, select


metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("surname", String),
    Column("birth_date", Date, nullable=False),
)

DATABASE_URL = "postgresql+asyncpg://postgres:123@localhost/postgres"

async def main():
    # Создаем асинхронный движок и сессию
    engine = create_async_engine(DATABASE_URL, echo=True)
    async_session = sessionmaker(
        bind=engine, class_=AsyncSession, expire_on_commit=False
    )

    try:
        async with async_session() as session:
            # Выполнение запроса
            query = select(users_table)
            result = await session.execute(query)
            rows = result.fetchall()
            print(rows)
            for row in rows:
                print(row)
                
                
            query_2 = select(users_table.c.id, users_table.c.name).where(users_table.c.name == "Petr")
            result = await session.execute(query_2)
            james = result.fetchall()
            print(james)
    finally:
        # Закрываем движок
        await engine.dispose()

if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
