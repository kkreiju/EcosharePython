from flask import Flask # type: ignore
from flask_cors import CORS # type: ignore

def create_app():
    app = Flask(__name__)
    CORS(app)

    from .routes import api
    app.register_blueprint(api)

    return app
