import sqlite3
import datetime

id = 1
req = 5
times = datetime.datetime.now()

conn = sqlite3.connect("db.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()


def update_sqllite():
    cursor.execute("INSERT INTO `users` (`user_id`, `request`,'timestamp') VALUES(?,?,?)",
                   (id, req, times))


conn.commit()
