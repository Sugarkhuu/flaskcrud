# https://thepythoncode.com/article/building-crud-app-with-flask-and-sqlalchemy?utm_content=cmp-true
# pip install flask flask-sqlalchemy PyMySQL
# SET DEV_DATABASE_URL=postgresql://postgres:postgres@localhost:5432/mydatabase
# SET FLASK_APP=bookshop.py
# flask shell
# db.create_all()
# book = Book(author="Ezz", title="Cleaner Python", price=0.0)
# db.session.add(book)
# book2 = Book(author="Ahmed", title="Python", price=10.99)
# db.session.add(book2)
# book3 = Book(author="Altan", title="Erdene", price=15)
# db.session.add(book3)
# db.session.commit()

# docker-compose build
# docker-compose up -d postgres
# docker-compose up -d flask_app


# SET FLASK_APP=bookshop.py
# flask run
# http://127.0.0.1:5000/book/list


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    return app