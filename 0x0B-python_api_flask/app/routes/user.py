from flask import Blueprint, Request, jsonify
from app.models.user import User

user_bp = Blueprint('user',__name__)

@user_bp.rout("/register", methods=["POST"])
def register():
    username = Request.jso.get('username')
    password = Request.jso.get('password')
    email = Request.json.get('email')

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify(message='username already token'), 409