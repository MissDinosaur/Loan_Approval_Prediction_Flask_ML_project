"""
This module serves as the entry point for the Flask application.

It performs the following tasks:
1. Opens the default web browser and navigates to the application's
index page (http://127.0.0.1:5000/index) only when the application is run for
the first time.
2. Starts the Flask development server with the specified host (127.0.0.1)
and port (5000).
3. Enables debugging mode to facilitate easier development and error handling.

Modules:
    webbrowser - Used to open the web browser automatically when the
    server starts. os - Provides access to operating system functionality
    to check for the first execution of the application.app - The Flask
    application instance, imported from the app module.

Usage:
    This module should be executed directly to run the Flask server.
"""
import webbrowser
import os
from app import app

if __name__ == '__main__':
    # Open browser only if this is the first execution
    # (not Flask's auto-reload)
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        webbrowser.open("http://127.0.0.1:5000/index")

    # Start the Flask server
    app.run(host='127.0.0.1', port=5000, debug=True)
