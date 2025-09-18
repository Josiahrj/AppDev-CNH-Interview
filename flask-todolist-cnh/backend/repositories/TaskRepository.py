from models.TaskModel import Task
from extensions import db
from flask import jsonify

# Repository layer: responsible for direct database interactions
# (CRUD operations for Task objects)
class TaskRepository:
    # Fetch all tasks from the database
    def get_tasks(self):
        return Task.query.all()

    # Add a new task to the database
    def add_task(self, description, completed=False):
        # Create a new Task object
        task = Task(description=description, completed=completed)

        # Persist the task into the database
        # (session.add + session.commit ensures it is saved)
        db.session.add(task)
        db.session.commit()

        return task
    
    # Delete a task by its ID
    def delete_task(self, taskId):
        # Look up task by primary key (id)
        task = Task.query.get(taskId)

        # If no task exists with that ID, return an error
        if not task:
            return jsonify({"error": "Task not found"}), 404

        # Remove task from database and save changes
        db.session.delete(task)
        db.session.commit()

        return jsonify({"message": "Task deleted"}), 200
