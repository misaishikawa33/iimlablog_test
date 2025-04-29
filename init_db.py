# データベースの初期化

# init_db.py
import sqlite3

def init():
    conn = sqlite3.connect('example.db')  # ファイル名は app.py などと一致させてください
    c = conn.cursor()

    # users テーブルを作成
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init()
