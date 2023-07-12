from app import db

class User(db.Model):
    id = db.column(db.String(100), primary_key=True)
    username =db.column(db.String(100), unqiue=True, unllable=False)
    password =db.column(db.String(255), nullable=False)
    email =db.column(db.String(100), unqiue=True, nullable=False)