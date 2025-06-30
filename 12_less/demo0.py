from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table, select

DATABASE_URL = "postgresql+asyncpg://postgres:123@localhost/postgres"

async def main():
    # 1. Создаём движок
    engine = create_async_engine(DATABASE_URL)
    
    # 2. Создаём метаданные
    metadata = MetaData()
    
    # 3. Подгружаем таблицу из БД через run_sync
    async with engine.begin() as conn:
        # Функция ДОЛЖНА принимать соединение как аргумент
        def sync_reflect(sync_conn):
            return Table(
                "users",
                metadata,
                autoload_with=sync_conn  # Используем переданное соединение
            )
        
        users_table = await conn.run_sync(sync_reflect)
    
    # Теперь таблица готова к использованию
    print("Структура таблицы:", users_table.columns.keys())
    
    # 4. Работаем с таблицей через сессию
    async_session = sessionmaker(engine, class_=AsyncSession)
    async with async_session() as session:
        result = await session.execute(select(users_table))
        rows = result.fetchall()
        print("Данные:", rows)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())