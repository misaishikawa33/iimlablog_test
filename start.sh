#!/bin/bash
# 起動順番

python init_db.py    # DB 初期化
gunicorn app:app     # Flask アプリ起動
