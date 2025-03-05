import webbrowser
import os
from app import app

if __name__ == '__main__':
    # Open browser only if this is the first execution (not Flask's auto-reload)
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        webbrowser.open("http://127.0.0.1:5000/index")

    # Start the Flask server
    app.run(host='127.0.0.1', port=5000, debug=True)