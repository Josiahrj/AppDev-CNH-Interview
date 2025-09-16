from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://cnh_interview_postgresql_user:7K66Q2Y3W5MoeGaeOYsjoCHRd0urroQ3@dpg-d34v4d0dl3ps73883ht0-a/cnh_interview_postgresql"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models.TaskModel import Task

with app.app_context():
    db.create_all()

from controllers.TaskController import task_blueprint
app.register_blueprint(task_blueprint, url_prefix="/tasks")

if __name__ == "__main__":
    import os

    # Use the PORT environment variable when available (Render / other hosts set this).
    port = int(os.environ.get("PORT", 5000))

    # Only enable debug when explicitly requested (e.g. FLASK_DEBUG=1 on your dev machine)
    debug_mode = os.environ.get("FLASK_DEBUG", "0") == "1"

    # Bind to 0.0.0.0 so the server is reachable from outside the container/VM
    app.run(host="0.0.0.0", port=port, debug=debug_mode)