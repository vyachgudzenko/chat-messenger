import sqlite3
import time
from operator import itemgetter

class DataBase(object):
    """Базовый класс подключения и работы с базами данных"""
    def create_table_users(self):
        """
        Создание новой таблицы пользователей
        """
        self.cursor.execute("""
                       CREATE TABLE users(
                       user text,
                       password text)""")

    def create_table_messages(self):
        """
        Создание новой таблицы сообщений
        """
        self.cursor.execute("""
                       CREATE TABLE messages(
                       sender text,
                       message text,
                       time float)""")
        print('Таблица создана')

    def is_unique(self, user):
        """
        Проверка на уникальность пользователя
        return True если такой пользователь уже есть
        """
        query = """SELECT user,password FROM users WHERE user = ?"""
        self.cursor.execute(query,(user,))
        if self.cursor.fetchone():
            return False
        else:
            return True

    def add_user(self, user,password):
        """
        Добавление нового пользователя
        """
        user = user.lower()
        if self.is_unique(user):
            self.cursor.execute("""
                            INSERT INTO users VALUES(?,?)
                            """,(user,password))
            self.connection.commit()
            print('Пользователь добавлен')
        else:
            print('Такой пользователь уже существуюет')

    def authorization(self,user,password):
        """
        Проверка авторизационных данных пользователя
        """
        query = """SELECT password FROM users WHERE user = ?"""
        self.cursor.execute(query,(user,))
        response = self.cursor.fetchone()
        if response:
            user_password = response[0]
            if user_password == password:
                return True
        else:
            return False

    def send_message(self,user,message):
        """
        Сохранение сообщения в базе данных
        user: имя пользователя,
        message: текст сообщения,
        time: время сохоанения
        """
        self.cursor.execute("""
                        INSERT INTO messages VALUES(?,?,?)
                        """,(user,message,time.time()))
        self.connection.commit()

    def get_messages_after(self,time):
        """
        Возвращает список кортежей с сообщениями,
        отобранными после времени time
        """
        query = """SELECT * FROM messages WHERE time > ?"""
        self.cursor.execute(query,(time,))
        messages = self.cursor.fetchall()
        return messages

class SQLite3DB(DataBase):
    """Класс подключения """
#'messanger_db.db'
    def __init__(self,database_name):
        self.connection = sqlite3.connect(database_name,check_same_thread=False)
        self.cursor = self.connection.cursor()

if __name__ == '__main__':
    s = SQLite3DB('messanger_db.db')
    m = s.get_messages_after(0)
    for i in m:
        print(i)
