from app import website
from flask import Flask
from http import HTTPStatus


def create_app():
    app = Flask(__name__)
    app.register_blueprint(website.bp)

    @app.route('/health', methods=['GET'])
    def health():
        """ Just a health check endpoint. """
        return 'Healthy', HTTPStatus.OK

    return app
