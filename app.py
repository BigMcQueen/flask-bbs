from datetime import datetime
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from pytz import timezone

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone('Asia/Tokyo')))
    username = db.Column(db.String(20))
    email = db.Column(db.String)
    write = db.Column(db.String(200), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        posts = User.query.all()
        return render_template('index.html', posts=posts)
    else: 
        if len(request.form.get('username')) == 0:
            username = '名無し'
        elif len(request.form.get('username')) > 20:
            return render_template('redo.html')
        else:
            username = request.form.get('username')
        email = request.form.get('email')
        if (len(request.form.get('write')) == 0) | (len(request.form.get('write')) > 200):
            return render_template('redo.html')
        else:
            write = request.form.get('write')

        new_post = User(username=username, email=email, write=write)

        db.session.add(new_post)
        db.session.commit()
        return redirect('/')

if __name__ == '__main__':
    app.run()