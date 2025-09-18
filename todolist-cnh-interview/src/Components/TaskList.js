import React, { useEffect, useState } from "react";
import InputForm from "./InputForm";

// Base URL for the backend API
const API_URL = "http://127.0.0.1:5001";

function TaskList() {
  // React state to hold tasks fetched from the backend
  const [tasks, setTasks] = useState([]);

  // useEffect hook runs once on component mount to fetch initial tasks
  useEffect(() => {
    fetchTasks();
  }, []);

  // Fetch all tasks from the backend
  const fetchTasks = async () => {
    try {
      const response = await fetch(`${API_URL}/get_all_tasks`); // GET request to backend
      if (!response.ok) throw new Error("Failed to fetch tasks");

      const data = await response.json(); // Parse JSON response
      setTasks(data); // Update state with fetched tasks
    } catch (err) {
      console.error("Error fetching tasks:", err);
    }
  };

  // Add a new task to the backend and update UI
  const addTask = async (description) => {
    // Prevent adding empty or whitespace-only tasks
    if (description.trim() === "") return;

    try {
      const response = await fetch(`${API_URL}/add_task`, {
        method: "POST", // POST request
        headers: { "Content-Type": "application/json" }, // Sending JSON
        body: JSON.stringify({ description }), // Request body
      });

      if (!response.ok) throw new Error("Failed to create task");

      const newTask = await response.json(); // Parse new task from response
      setTasks([...tasks, newTask]); // Add new task to state
    } catch (err) {
      console.error("Error adding task:", err);
    }
  };

  // Delete a task by ID
  const deleteTask = async (id) => {
    try {
      const response = await fetch(`${API_URL}/delete_task`, {
        method: "DELETE", // DELETE request
        mode: "cors", // Enable cross-origin requests
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ taskId: id }), // Pass taskId to backend
      });

      if (!response.ok) throw new Error("Failed to delete task");

      // Update state by filtering out the deleted task
      setTasks(tasks.filter((task) => task.id !== id));
    } catch (err) {
      console.error("Error deleting task:", err);
    }
  };

  // Render task list UI
  return (
    <div>
      {/* Input form for adding new tasks */}
      <InputForm onAdd={addTask} />

      {/* List of tasks */}
      <ul className="task-list">
        {tasks.map((task) => (
          <li key={task.id} className="task-item">
            <span>{task.description}</span>
            {/* Delete button for each task */}
            <button onClick={() => deleteTask(task.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TaskList;
