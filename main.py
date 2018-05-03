from flask import Flask, render_template
from flask_socketio import SocketIO, emit

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app, async_mode=async_mode)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/test')
def test():
    return 'test'

@socketio.on('myevent')
def test_message(message):
    emit('myresponse', {'data': 'got it!'})
    
@socketio.on('chat message')
def test_message(message):
    emit('chat message', message)

if __name__ == '__main__':
    app.run()
