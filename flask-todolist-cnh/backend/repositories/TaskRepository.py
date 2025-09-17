from models.TaskModel import Task
from extensions import db
from flask import jsonify

class TaskRepository:
    def get_tasks(self):
        return Task.query.all()

    def add_task(self, description, completed=False):
        task = Task(description=description, completed=completed)

        # Not sure id keep this here or in orchestrator
        db.session.add(task)
        db.session.commit()

        return task
    
    def delete_task(self, taskId):
        task = Task.query.get(taskId)

        if not task:
            return jsonify({"error": "Task not found"}), 404

        db.session.delete(task)
        db.session.commit()

        return jsonify({"message": "Task deleted"}), 200