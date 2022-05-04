import psycopg2

conn = psycopg2.connect(dbname='suppliers', user='postgres', password='123qwe123', host='localhost')
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()
print(results)