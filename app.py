from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# SQLiteデータベースの初期化
def init_db():
    conn = sqlite3.connect('example.db')  # SQLiteデータベースファイルを作成または接続
    c = conn.cursor()
    # usersテーブルを作成（存在しない場合のみ）
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

# ユーザーをデータベースに追加
def insert_user(name, email):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

# データベースからすべてのユーザーを取得
def get_all_users():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()  # すべてのユーザーを取得
    conn.close()
    return users

# ホーム画面（すべてのユーザーを表示）
@app.route('/')
def index():
    users = get_all_users()  # データベースからユーザーを取得
    return render_template('index.html', users=users)

# ユーザー追加画面（フォーム送信を受け付ける）
@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']  # フォームからnameを取得
    email = request.form['email']  # フォームからemailを取得
    insert_user(name, email)  # ユーザー情報をデータベースに追加
    return redirect(url_for('index'))  # ユーザー追加後にホーム画面にリダイレクト

if __name__ == '__main__':
    init_db()  # アプリ起動時にデータベースを初期化
    app.run(debug=True)
