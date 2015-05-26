from werkzeug.security import generate_password_hash, check_password_hash
from application.database import GetUserId, GetUserPwHash


def valid_user(username, password):
    valid = False

    userId = GetUserId(username)

    if userId:
        userPwHash = GetUserPwHash(userId)

        if userPwHash:

            if check_password_hash(userPwHash, password):
                valid = True

    return valid
