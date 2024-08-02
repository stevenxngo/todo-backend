from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flasgger import Swagger  # Import Swagger

db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):
    app = Flask(__name__)

    # Default configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SWAGGER'] = {
        'title': 'TODO API Server',
        'uiversion': 3
    }

    if config:
        app.config.update(config)

    # Initialize SQLAlchemy, Migrate, and Swagger
    db.init_app(app)
    migrate.init_app(app, db)
    Swagger(app)  # Initialize Swagger

    # Enable CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    # Import and setup routes
    from .routes import setup_routes
    setup_routes(app)

    @app.after_request
    def handle_options(response):
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, X-Requested-With"
        return response

    return app
