import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="sales_admin",
    password="SoPro1234",
    database="sales_db",
    port=3307
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM route")

res = cursor.fetchall()

conn.close()

for row in res:
    print({"id": row[0], "route": row[1]})
