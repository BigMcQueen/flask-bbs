# Flask を使った掲示板

## 使用機器

Macbook Air(M1, 2020)

## 開発環境

venv(python:3.9.6)
<br>
SQLite

## db の作成方法

ターミナルで python3 を開く　　
<br>

- from app import app
- from app import db
- with app.app_context(): db.create_all()
- instance フォルダが作成され、その中に project.db があることを確認する
- exit()　
  <br>
  python3 から抜ける

## 使い方

- 200 文字以内でコメントを書き込むことができます。
- 名前を入力しなかった場合、表示が「名無し」になります。
- 名前、コメント内容が規定の文字数以外だと、エラーページに遷移します。
- 100 件までコメントを書き込むことができます。

## 見本

![ScreenShot 2022-12-31 0 18 39](https://user-images.githubusercontent.com/86920995/210122608-a09507a6-92c3-4592-b80f-e900931ea4d4.JPG)
