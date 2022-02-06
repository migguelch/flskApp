from flask import Flask

def create_app():
    app = Flask(__name__)

    #BluePrints
    from .public import public_Blueprint
    app.register_blueprint(public_Blueprint)


    return app
