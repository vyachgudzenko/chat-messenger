import sqlite3
import time
from operator import itemgetter

connection = sqlite3.connect('messanger_db.db',check_same_thread=False)
cursor = connection.cursor()

def create_table_users():
    """
    Создание новой таблицы пользователей
    """
    cursor.execute("""
                   CREATE TABLE users(
                   user text,
                   password text)""")
    print('Таблица создана')

def create_table_messages():
    """
    Создание новой таблицы сообщений
    """
    cursor.execute("""
                   CREATE TABLE messages(
                   sender text,
                   message text,
                   time float)""")
    print('Таблица создана')

def is_unique(user):
    """
    Проверка на уникальность пользователя
    return True если такой пользователь уже есть
    """
    query = """SELECT user,password FROM users WHERE user = ?"""
    cursor.execute(query,(user,))
    if cursor.fetchone():
        return False
    else:
        return True

def add_user(user,password):
    """
    Добавление нового пользователя
    """
    user = user.lower()
    if is_unique(user):
        cursor.execute("""
                        INSERT INTO users VALUES(?,?)
                        """,(user,password))
        connection.commit()
        print('Пользователь добавлен')
    else:
        print('Такой пользователь уже существуюет')

def authorization(user,password):
    """
    Проверка авторизационных данных пользователя
    """
    query = """SELECT password FROM users WHERE user = ?"""
    cursor.execute(query,(user,))
    response = cursor.fetchone()
    if response:
        user_password = response[0]
        if user_password == password:
            return True
    else:
        return False

def send_message(user,message):
    """
    Сохранение сообщения в базе данных
    user: имя пользователя,
    message: текст сообщения,
    time: время сохоанения
    """
    cursor.execute("""
                    INSERT INTO messages VALUES(?,?,?)
                    """,(user,message,time.time()))
    connection.commit()

def get_messages_after(time):
    """
    Возвращает список кортежей с сообщениями,
    отобранными после времени time
    """
    query = """SELECT * FROM messages WHERE time > %s""" % time
    cursor.execute(query)
    messages = cursor.fetchall()
    return messages
