import psycopg2

connection = psycopg2.connect(
    dbname="dbname",
    user="user",
    host="host",
    password="password",
    port="port"
)

cursor = connection.cursor()


cursor.execute('select * from table_name')

result = cursor.fetchall()

for i in result:
    print(i)

    