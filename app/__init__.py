# https://thepythoncode.com/article/building-crud-app-with-flask-and-sqlalchemy?utm_content=cmp-true
# pip install flask flask-sqlalchemy PyMySQL
# SET DEV_DATABASE_URL=postgresql://myuser:mypassword@localhost:5056/mydatabase
# SET FLASK_APP=bookshop.py
# flask shell
# db.create_all()
# book = Book(author="Ezz", title="Cleaner Python", price=0.0)
# db.session.add(book)
# db.session.commit()
# book2 = Book(author="Ahmed", title="Python", price=10.99)
# db.session.add(book2)
# db.session.commit()


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