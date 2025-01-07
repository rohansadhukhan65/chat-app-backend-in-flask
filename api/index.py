from flask import Flask
from flask_socketio import SocketIO , emit

# Initialize Flask app and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'


@socketio.on('connect')
def handle_connect():
    print("🔌 Socket Connected 🟢")