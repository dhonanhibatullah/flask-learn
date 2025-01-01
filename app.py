from flask import Flask
import apps.Authentication.routes as authentication
import apps.Healthcheck.routes as healthcheck

app = Flask(__name__)
authentication.register_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)