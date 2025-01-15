import psycopg2

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="123",  # Укажите здесь ваш пароль
    host="localhost",          # Явно указываем хост
    port="5432"                # Not important
)

print(conn)
cur = conn.cursor()
print(cur)

res = cur.execute("Select * FROM users;")
print(res)

users = cur.fetchall()
print(users)

try:
    cur.execute("INSERT INTO users(name, surname) VALUES ('Petr', 'Petress');")
    conn.commit()  # Подтверждаем изменения
except Exception as e:
    print("Ошибка при вставке данных:", e)
    
conn.close()