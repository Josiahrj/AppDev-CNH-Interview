from flask import Blueprint, jsonify, request
from orchestrators.TaskOrchestrator import TaskOrchestrator

task_blueprint = Blueprint("task_blueprint", __name__)
taskOrchestrator = TaskOrchestrator()

@task_blueprint.route("/get_all_tasks", methods=["GET"])
def get_tasks():
    tasks = taskOrchestrator.get_all_tasks()
    return jsonify([t.to_dict() for t in tasks])

@task_blueprint.route("/add_task", methods=["POST"])
def create_task():
    data = request.get_json()

    description = data.get("description")
    task = taskOrchestrator.create_task(description, False)

    return jsonify(task.to_dict()), 201

@task_blueprint.route("/delete_task", methods=["DELETE"])
def delete_task():
    data = request.get_json()
    id = data.get("taskId")
    if not id:
        return jsonify({"error": "taskId is required"}), 400

    code = taskOrchestrator.delete_task(id)
    return jsonify({"status": "deleted", "task_id": id}), 200
