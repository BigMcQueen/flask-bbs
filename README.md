# flask-bbs
## dbの作成方法
- ターミナルでpython3を開く
- from app import app
- from app import db
- with app.app_context():
	  db.create_all()
- instanceフォルダが作成され、その中にproject.dbがあることを確認する
- exit()
- python3から抜ける
## 見本
![ScreenShot 2022-12-31 0 07 16](https://user-images.githubusercontent.com/86920995/210084802-c5b3055b-9586-4246-8fc2-de6e02bbfcfa.JPG)
