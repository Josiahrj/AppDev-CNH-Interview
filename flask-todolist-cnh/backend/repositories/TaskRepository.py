from models.TaskModel import Task
from app import db

class TaskRepository:
    def get_tasks(self):
        return Task.query.all()

    def add_task(self, description, completed=False):
        task = Task(description=description, completed=completed)

        # Not sure id keep this here or in orchestrator
        db.session.add(task)
        db.session.commit()

        return task