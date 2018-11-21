from flask import current_app

from project import bcrypt


def __init__(self, username, email, password):
    self.username = username
    self.email = email
    # new
    self.password = bcrypt.generate_password_hash(
        password, current_app.config.get('BCRYPT_LOG_ROUNDS')
    ).decode()
