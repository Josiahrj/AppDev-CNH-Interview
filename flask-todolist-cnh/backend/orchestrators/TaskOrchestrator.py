from repositories.TaskRepository import TaskRepository

# Orchestrator layer that handles business logic for tasks.
# It acts as a middle layer between controllers (API endpoints) and repositories (DB layer).
class TaskOrchestrator:
    def __init__(self):
        # Initialize the repository object, which directly interacts with the database
        self.repo = TaskRepository()

    # Get all tasks from the database (delegates to repository)
    def get_all_tasks(self):
        return self.repo.get_tasks()

    # Create a new task with a description and optional "completed" status
    def create_task(self, description, completed=False):
        return self.repo.add_task(description, completed)
    
    # Delete a task by its ID
    def delete_task(self, taskId):
        return self.repo.delete_task(taskId)
