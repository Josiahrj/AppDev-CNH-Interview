from repositories.TaskRepository import TaskRepository

class TaskOrchestrator:
    def __init__(self):
        self.repo = TaskRepository()

    def get_all_tasks(self):
        return self.repo.get_tasks()

    def create_task(self, description, completed=False):
        return self.repo.add_task(description, completed)
    
    def delete_task(self, taskId):
        return self.repo.delete_task(taskId)