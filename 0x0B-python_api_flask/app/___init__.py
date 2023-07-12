from flask import flask
from flask_sqlalchemy import SQLAlchemy

app = flask(__name__)
app.config['SQLACHEMY_DATABASE_URI'] = "sqlite://database.db"
app.config['SQLACHEMY_TRARCK_MODIFICATIONS'] = False
app.config['SQLCHEMY_KEY'] = "KEY-goes-here"
db = SQLAlchemy(app)