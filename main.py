import random
from flask import Flask, make_response, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)


# Определение моделей данных
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    completed_tables = db.Column(db.Integer, default=0)
    total_tables = db.Column(db.Integer, default=0)
    completed_tasks = db.Column(db.Integer, default=0)
    total_tasks = db.Column(db.Integer, default=0)
    registration_time = db.Column(db.DateTime, nullable=False)

    tables = db.relationship('Table', secondary='user_table', back_populates='users')
    tasks = db.relationship('Task', back_populates='author')


class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_name = db.Column(db.String(80), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', back_populates='tables')
    tasks = db.relationship('Task', secondary='table_task', back_populates='tables')


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_number = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(200), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', back_populates='tasks')
    image = db.Column(db.String(200))
    description = db.Column(db.String(200))
    completion_percentage = db.Column(db.Integer)


# Создание таблиц
db.create_all()
themes = ["neon", "monohrom", "beer", "xeon", "etti", "sea", "deep_ocean", "christmas"]


@app.route('/')
def tasks():
    resp = make_response(render_template("tasks.html", theme=themes[random.randint(0, 7)]))
    try:
        key = request.cookies.get('key')
    except:
        resp.set_cookie('key', 'I am cookie')
    return resp


if __name__ == '__main__':
    app.run(debug=True)
