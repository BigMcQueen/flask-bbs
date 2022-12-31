# Flaskを使った掲示板
## 使用機器
Macbook Air(M1, 2020)
## 開発環境
venv(python:3.9.6)
<br>
SQLite
## dbの作成方法
ターミナルでpython3を開く　　
<br>
- from app import app　
- from app import db　　
- with app.app_context():   db.create_all()　　
- instanceフォルダが作成され、その中にproject.dbがあることを確認する　　
- exit()　
<br>
python3から抜ける　　

## 見本
![ScreenShot 2022-12-31 0 18 39](https://user-images.githubusercontent.com/86920995/210122608-a09507a6-92c3-4592-b80f-e900931ea4d4.JPG)
