from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("execute")
def handle_commands(data):
    # Simulate command execution
    for command in data["commands"]:
        # Process the command and send updates to the simulator
        socketio.emit("simulation_update", {
            "command": command,
            "status": "executed"
        })

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
