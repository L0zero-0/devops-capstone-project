from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

# Initialize Talisman for security headers
talisman = Talisman()

# Initialize CORS for cross-origin resource sharing
cors = CORS()

def create_app():
    """ Initialize the core application """
    app = Flask(__name__)
    
    # Load configuration and routes...
    
    # Initialize extensions with the Flask app
    talisman.init_app(app)
    cors.init_app(app)
    
    return app
