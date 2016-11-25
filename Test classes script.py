import MySQLdb
import random

class Connection:
    def __init__(self, user, password, db, host=''):
        self.user = user
        self.password = password
        self.db = db
        self._connection = None

    @property
    def connection(self):
        self.connect()
        return self._connection

    def close(self):
        if self._connection:
            self._connection.close()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host="127.0.0.1",
                user=self.user,
                passwd=self.password,
                db=self.db,
                charset="utf8"
            )


class Books:
    def __init__(self, db, name, author, description):
        self.db = db
        self.name = name
        self.author = author
        self.description = description

    def save(self):
        cursor = self.db.connection.cursor()
        cursor.execute(
            "INSERT INTO Books (name, author, description) VALUES(%s, %s, %s)",
            (self.name, self.author, self.description))
        self.db.connection.commit()
        cursor.close()

    @staticmethod
    def select_all(db):
        cursor = db.connection.cursor()
        cursor.execute(
            "SELECT * from Books")
        selected = cursor.fetchall()
        cursor.close()
        return selected


db = Connection("labs", "0000", "labs", "127.0.0.1")

b = Books(db, "Властелин колец", "Толкиен", "Трилогия")
b.save()

books = list(Books.select_all(db))
print(books)

db.close()
