import mysql.connector as mysql


def get_db():
    config = {
        "user": "root",
        "password": "root",
        "host": "localhost",
        "port": 3306,
    }
    db = mysql.connect(**config)
    return db


def create_db(cursor, db_db):
    cursor.execute('CREATE DATABASE IF NOT EXISTS {}'.format(db_db))
    return


def create_table(cursor, db_db, db_table):
    cursor.execute('USE {}'.format(db_db))
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS {} (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, URL VARCHAR(2083))'.format(db_table))
    return


def insert_into(cursor, db, db_table, url):
    query_insert = 'INSERT INTO {} VALUES (%s, %s)'.format(db_table)
    cursor.execute(query_insert, (None, url))
    db.commit()
    return


def select_from(cursor, db_table, url):
    query_select = 'SELECT URL FROM {} WHERE URL = %s'.format(db_table)
    cursor.execute(query_select, (url, ))
    results = cursor.fetchall()
    return results[0]


def close_connection(cursor, db):
    cursor.close()
    db.close()
    return


if __name__ == '__main__':
    pass
