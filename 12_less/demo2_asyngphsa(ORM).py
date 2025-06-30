from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table, Column, Integer, String, Date, select, func


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
    engine = create_async_engine(DATABASE_URL, echo=True) #
    async_session = sessionmaker(
        bind=engine, class_=AsyncSession, expire_on_commit=False
    )

    try:
        async with async_session() as session:
            # Выполнение запроса
            query = select(users_table).order_by(users_table.c.id)
            result = await session.execute(query)
            rows = result.fetchall()
            print(rows)
            for row in rows:
                print(row)
                
            print('-------------------------------------------------')    
            query_2 = select(users_table.c.id, users_table.c.name).where(users_table.c.name == "Petr")
            result = await session.execute(query_2)
            james = result.fetchall()
            print(james)
            
            
            
            
            # 1. fetchall() — все записи
            result = await session.execute(select(users_table).order_by(users_table.c.id))
            all_users = result.fetchall()
            print("Все пользователи:", all_users)
            print('-------------------------------------------------')  
            # 2. fetchone() — только первая запись (но можно продолжить чтение)
            result = await session.execute(select(users_table))
            first_user = result.fetchone()
            print("Первая запись:", first_user)
            print('-------------------------------------------------')  
            # 3. first() — первая запись (курсор закрыт)
            result = await session.execute(select(users_table))
            first_user_closed = result.first()
            print("Первая запись (закрытый курсор):", first_user_closed)
            print('-------------------------------------------------')  
            # 4. scalar() — например, количество пользователей
            result = await session.execute(select(func.count(users_table.c.id)))
            total = result.scalar()
            print("Всего пользователей:", total)
    finally:
        # Закрываем движок
        await engine.dispose()

if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
