from flask import Flask
from flask_socketio import SocketIO , emit


# Initialize Flask app and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return "Hello 👋!"

@socketio.on('connect')
def handle_connect():
    print("🔌 Socket Connected 🟢")
    

#! Run the app with SocketIO
if __name__ == '__main__':
    socketio.run(app, debug=True)