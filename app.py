import os

from flask_sqlalchemy import SQLAlchemy

from datetime import datetime
import time

from flask import Flask, render_template, request, redirect, url_for
import numpy as np

app = Flask(__name__)
db_path = os.path.join(os.path.dirname(__file__), 'test2.db')
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'entries'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    date = db.Column(db.DateTime)

    comment = db.relationship("UserComment", backref='user', lazy='dynamic')


    def __init__(self, name, datetime):
        self.name = name
        self.date = datetime

    def __repr__(self):
        return '<Name %r>' % self.name

    def add_comment(self, comment):
        self.comment = comment

class UserComment(db.Model):
    __tablename__='comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text)
    date = db.Column(db.DateTime)

    comment_id = db.Column(db.Integer, db.ForeignKey('entries.id'))

    def __init__(self, comment, date, e_id):
        self.comment = comment
        self.date = date
        self.comment_id = e_id

    def __repr__(self):
        return '<comment %r>' % self.comment

def picked_up():
    messages = [
        "こんにちは、あなたの名前を入力してください",
        "やあ！お名前は何ですか？",
        "あなたの名前を教えてね"
    ]
    return np.random.choice(messages)

@app.route('/')
def index():
    title = "ようこそ"
    message = picked_up()
    return render_template('index.html',
                           message=message, title=title)

if __name__ == '__main__':
    #app.debug = True # デバッグモード有効化
    #port = int(os.environ.get('PORT', 5000))
    #app.run(port=port)
    app.run()
