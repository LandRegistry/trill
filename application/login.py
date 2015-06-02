from werkzeug.security import generate_password_hash, check_password_hash
from application.database import GetUserId, GetUserPwHash
from itsdangerous import URLSafeTimedSerializer
from application import app

ts = URLSafeTimedSerializer(app.config["SECRET_KEY"])

def valid_user(username, password):
    valid = False

    userId = GetUserId(username)

    if userId:
        userPwHash = GetUserPwHash(userId)

        if userPwHash:

            if check_password_hash(userPwHash, password):
                valid = True

    return valid

def create_hash(password):
    pwhash = generate_password_hash(password)
    
    return pwhash
