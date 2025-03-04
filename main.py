import webbrowser
# Flask entry point
from app import app  # Import Flask app from __init__.py

if __name__ == '__main__':
    # Open the default web browser to the homepage
    webbrowser.open("http://127.0.0.1:5000/index")
    
    # Start the Flask server
    app.run(host='127.0.0.1', port=5000, debug=True)