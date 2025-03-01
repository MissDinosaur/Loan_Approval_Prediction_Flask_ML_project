from flask import Flask
"""
Only in Flask Applications, __init__.py is used to create app, import routes, and set up configs.
"""

# Initialize flask app
app = Flask(__name__, template_folder='templates')

from app import routes  # Import routes AFTER app is created
