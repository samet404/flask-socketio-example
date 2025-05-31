from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

socketio = SocketIO(cors_allowed_origins="*")  # Allow all origins

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    CORS(app)  # Enable CORS for all routes
    socketio.init_app(app)
    return app


if __name__ == '__main__':
    app = create_app()

    @app.route('/', methods=['GET'])
    def index():
        return '<h1>Hello, World!</h1>', 200


    @socketio.on('message', namespace='/ws')
    def handle_message(data):
        print('received message: ' + data)


    @socketio.on('json', namespace='/ws')
    def handle_json(json):
        print('received json: ' + str(json))

    @socketio.on('my event', namespace='/ws')
    def handle_my_custom_event(json):
        print('received json: ' + str(json))
        emit('my response', {'data': 'got it!'}, namespace='/ws')


    socketio.run(app, debug=True, port=4000)  # Remove the additional app.run()
