from flask import Blueprint, jsonify, request
from orchestrators.TaskOrchestrator import TaskOrchestrator

task_blueprint = Blueprint("task_blueprint", __name__)
taskOrchestrator = TaskOrchestrator()

@task_blueprint("/", methods=["GET"])
def get_tasks():
    tasks = taskOrchestrator.get_all_tasks()
    return jsonify([t.todict() for t in tasks])

@task_blueprint("/add_task", methods=["POST"])
def create_task():
    data = request.get_json()

    description = data.get("description")
    task = taskOrchestrator.create_task(description, False)

    return jsonify(task.to_dict()), 201

