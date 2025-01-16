import psycopg2

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="123",  # Укажите здесь ваш пароль
    host="localhost",          # Явно указываем хост
    port="5432"                # Not important
)