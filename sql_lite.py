import sqlite3


def create_db(token, secret_key, language):
    connect_db = sqlite3.connect('db_for_dadata.db')
    cur = connect_db.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS tab
                (token text,
                secret_key text,
                language text)
                ''')
    data = (token, secret_key, language)
    cur.execute("insert into tab values (?,?,?)", data)
    connect_db.commit()


def get_data_db():
    connect_db = sqlite3.connect('db_for_dadata.db')
    cur = connect_db.cursor()
    cur.execute("SELECT * FROM tab")
    data = cur.fetchall()
    connect_db.commit()
    return data


def delete_db():
    connect_db = sqlite3.connect('db_for_dadata.db')
    cur = connect_db.cursor()
    cur.execute('''DROP TABLE IF EXISTS tab''')
    connect_db.commit()
