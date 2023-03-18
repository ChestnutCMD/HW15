import sqlite3


def connect(query):
    with sqlite3.connect("animal.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

        return result
