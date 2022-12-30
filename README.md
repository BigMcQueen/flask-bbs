# flask-bbs
## dbの作成方法
ターミナルでpython3を開く
- from app import app
- from app import db
- with app.app_context():
	  db.create_all()
instanceフォルダが作成され、その中にproject.dbがあることを確認する
- exit()
python3から抜ける
