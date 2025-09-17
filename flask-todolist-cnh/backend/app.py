from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from extensions import db

app = Flask(__name__)
CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    supports_credentials=True,
    methods=["GET", "POST", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type"]
)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://cnh_interview_user@localhost:5432/cnh_interview"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
db.init_app(app)

from models.TaskModel import Task

with app.app_context():
    db.create_all()

from controllers.TaskController import task_blueprint
app.register_blueprint(task_blueprint)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

if __name__ == "__main__":
    app.run(port=5001)