from flask import Flask, render_template
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

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)