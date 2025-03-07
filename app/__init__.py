from flask import Flask
from flask_caching import Cache
"""
__init__.py marks the folder as a Python package.
And in Flask Applications, __init__.py is also used to create app, import routes, and set up configs.
And use Flask-Caching to cache data and avoid recomputation for identical inputs.
It will enable faster responses.
"""

# Initialize flask app
app = Flask(__name__, template_folder='templates')
# Configure Flask-Caching (simple in-memory cache)
app.config['CACHE_TYPE'] = 'simple'
app.config['CACHE_DEFAULT_TIMEOUT'] = 300  # Cache expires in seconds (5 minutes)
cache = Cache(app)

from app import routes  # Import routes AFTER app is created
