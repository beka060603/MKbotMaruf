import sqlite3

__connection = None


def get_connection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect('mk.db')
        return __connection


def init_db(force: bool = False):
    conn = get_connection()
    c = conn.cursor()
    if force:
        c.execute('DROP TABLE IF EXISTS user_mesaage')

    c.execute('''
        CREATE TABLE IF NOT EXISTS user_massage(
            id          INTEGER PRiMARY KEY,
            user_id     INTEGER NOT NULL,
            text        TEXT NOT NULL
            )        
    ''')
    conn.commit()


def add_message(user_id: int, text: str):
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT INTO user_message (user_id, text) VALUES (?,?)', {user_id, text})
    conn.commit()


if __name__ == '__main__':
    init_db()

    add_message(user_id=1234, text='kekx')
