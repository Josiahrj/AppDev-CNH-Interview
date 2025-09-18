from flask import Blueprint, jsonify, request
from orchestrators.TaskOrchestrator import TaskOrchestrator

# Create a Flask Blueprint for task-related routes
task_blueprint = Blueprint("task_blueprint", __name__)

# Initialize the TaskOrchestrator, which handles the business logic for tasks
taskOrchestrator = TaskOrchestrator()

# -------------------------------
# Route: Get all tasks (READ)
# -------------------------------
@task_blueprint.route("/get_all_tasks", methods=["GET"])
def get_tasks():
    # Fetch all tasks from the orchestrator
    tasks = taskOrchestrator.get_all_tasks()
    # Convert each task to a dictionary and return as JSON
    return jsonify([t.to_dict() for t in tasks])

# -------------------------------
# Route: Create a new task (CREATE)
# -------------------------------
@task_blueprint.route("/add_task", methods=["POST"])
def create_task():
    # Parse JSON request body
    data = request.get_json()

    # Extract the description field
    description = data.get("description")

    # Create a new task with "completed" set to False by default
    task = taskOrchestrator.create_task(description, False)

    # Return the created task as JSON with 201 (Created) status
    return jsonify(task.to_dict()), 201

# -------------------------------
# Route: Delete a task (DELETE)
# -------------------------------
@task_blueprint.route("/delete_task", methods=["DELETE"])
def delete_task():
    # Parse JSON request body
    data = request.get_json()

    # Extract taskId from the request
    id = data.get("taskId")

    # If no taskId was provided, return a 400 error
    if not id:
        return jsonify({"error": "taskId is required"}), 400

    # Call orchestrator to delete the task
    code = taskOrchestrator.delete_task(id)

    # Return a success response with the deleted task ID
    return jsonify({"status": "deleted", "task_id": id}), 200
