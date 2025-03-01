# Flask entry point
from app import app  # Import Flask app from __init__.py

if __name__ == '__main__':
    app.run(host='5000', port=5000, debug=True)