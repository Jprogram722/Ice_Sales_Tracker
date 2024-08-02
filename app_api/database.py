import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


def connect():
    """
    This function will create a connection and a cursor to the database
    """
    try:
        conn = mysql.connector.connect(
            host="sales_db",
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE'),
            port=os.getenv('MYSQL_PORT')
        )

        cursor = conn.cursor()

        return conn, cursor

    except Exception as err:
        print(err)
        conn = None
        cursor = None

    return conn, cursor


if __name__ == "__main__":

    # This is just test code to make sure that I can grab data from the database

    conn, cursor = connect()

    cursor.execute("SELECT * FROM route")

    res = cursor.fetchall()

    conn.close()

    for row in res:
        print({"id": row[0], "route": row[1]})
