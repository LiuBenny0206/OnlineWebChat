from flask import Flask, render_template
import secrets
from flask_socketio import SocketIO, send


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)
socketio = SocketIO(app, cors_allowed_origins= "*")




@socketio.on('message')
def handle_message(message):
    print("Received message: "+ message)
    if message != "User connected!":
        send(message, broadcast=True)



@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


if __name__ == '__main__':
    socketio.run(app, host="127.0.0.1")
