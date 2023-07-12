from flask_jwt_extented import creat_access_token, jwt_required, get_jwt_identity
from flask import jsonify,current_app

def generate_token(user_id):
    creat_token = creat_access_token(identity=user_id)
    return creat_access_token

def verify(token):
    try:
        user_id = get_jwt_identity()
        return user_id
    except Exception as err:
        current_app.logger.error(str(err))
        return None