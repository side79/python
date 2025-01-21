import asyncio
import asyncpg
from datetime import date


# user="postgres",
# password="123", 
    
async def main():
    conn = await asyncpg.connect(
        'postgresql://postgres:123@localhost/postgres'
        # user='user', 
        # password='password',
        # database='database', 
        # host='127.0.0.1'
    )
    
    print(conn)
    
    # await conn.execute(
    #     "INSERT INTO users(name, surname, birth_date) VALUES($1, $2, $3)",
    #     "May", "MayMayMay", date(1972, 3, 13)
    # )
    
    # await conn.execute(
    #     """
    #     ALTER TABLE users 
    #     ADD COLUMN IF NOT EXISTS birth_date DATE
    #     """
    # )
    
    #values = await conn.fetch()
    
    rows = await conn.fetch("Select * from users")
    today = date.today()
    for r in rows:
        #print(r)
        if r["birth_date"]:
            age = today - r["birth_date"]
            print(f"Name: {r['name']}, Age: {age.days // 365} years")
        else:
            print(f"Name: {r['name']}, Birth date is not provided")
    await conn.close()

if __name__ == "__main__":
    asyncio.run(main())