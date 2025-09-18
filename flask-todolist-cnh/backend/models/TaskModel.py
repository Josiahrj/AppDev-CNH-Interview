from extensions import db

# Define the Task model, which maps to the "tasks" table in the database
class Task(db.Model):
    __tablename__ = 'tasks'  # Explicitly set the table name

    # Primary key column: unique ID for each task
    id = db.Column(db.Integer, primary_key=True)

    # Description of the task, required (cannot be null), max length 200 characters
    description = db.Column(db.String(200), nullable=False)

    # Boolean flag for whether the task is completed or not
    # Defaults to False when a new task is created
    completed = db.Column(db.Boolean, default=False)

    # Utility method: convert a Task object into a Python dictionary
    # Useful for serializing tasks to JSON for API responses
    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed
        }
