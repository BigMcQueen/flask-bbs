from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
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
    write = db.Column(db.String(200))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        posts = User.query.all()
        return render_template('index.html', posts=posts)
    else: 
        if len(request.form.get('username')) == 0:
            username = '名無し'
        else:
            username = request.form.get('username')
        email = request.form.get('email')
        write = request.form.get('write')

        new_post = User(username=username, email=email, write=write)

        db.session.add(new_post)
        db.session.commit()
        return redirect('/')

@app.route('/create')
def create():
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)