from flask import Flask
from flask_caching import Cache
"""
Only in Flask Applications, __init__.py is used to create app, import routes, and set up configs.
"""

# Initialize flask app
app = Flask(__name__, template_folder='templates')
# Configure Flask-Caching (simple in-memory cache)
app.config['CACHE_TYPE'] = 'simple'
app.config['CACHE_DEFAULT_TIMEOUT'] = 300  # Cache timeout in seconds (5 minutes)
cache = Cache(app)

from app import routes  # Import routes AFTER app is created
