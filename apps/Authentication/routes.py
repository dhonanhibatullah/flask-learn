from flask import Flask
from flask import Blueprint
from apps.Authentication.controllers import *

def register_routes(app: Flask):
    auth_bp = Blueprint('auth', __name__)

    auth_bp.route('/auth/register', methods=['POST'])(auth_register)
    auth_bp.route('/auth/login', methods=['POST'])(auth_login)

    app.register_blueprint(auth_bp)