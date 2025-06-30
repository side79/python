from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table, select, func

DATABASE_URL = "postgresql+asyncpg://postgres:123@localhost/postgres"

async def main():
    engine = create_async_engine(DATABASE_URL)
    
    metadata = MetaData()
    
    async with engine.begin() as conn:
        def sync_reflect(sync_conn):
            return Table(
                "users",
                metadata,
                autoload_with=sync_conn  # Используем переданное соединение
            )
        
        users_table = await conn.run_sync(sync_reflect)
    
    # Теперь таблица готова к использованию
    #print("Структура таблицы:", users_table.columns.keys())
    
    # 4. Работаем с таблицей через сессию
    async_session = sessionmaker(engine, class_=AsyncSession)
    
    
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

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())