from flask import request, Response, json
from apps.Authentication.services import AuthService

auth_service = AuthService()

def auth_register():
    req = request.get_json()
    res = auth_service.register(req)
    return Response(
        response    = json.dumps(res.get_response()),
        status      = res.get_status(),
        mimetype    = 'application/json'
    )

def auth_login():
    req = request.get_json()
    res = auth_service.login(req)
    return Response(
        response    = json.dumps(res.get_response()),
        status      = res.get_status(),
        mimetype    = 'application/json'
    )