import React, { useEffect, useState } from "react";
import InputForm from "./InputForm";

const API_URL = "http://127.0.0.1:5001";

function TaskList() {
  const [tasks, setTasks] = useState([]);

  // Fetch tasks on mount
  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      const response = await fetch(`${API_URL}/get_all_tasks`);
      if (!response.ok) throw new Error("Failed to fetch tasks");

      const data = await response.json();
      setTasks(data);
    } catch (err) {
      console.error("Error fetching tasks:", err);
    }
  };

  const addTask = async (description) => {
    if (description.trim() === "") return;

    try {
      const response = await fetch(`${API_URL}/add_task`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ description }),
      });

      if (!response.ok) throw new Error("Failed to create task");

      const newTask = await response.json();
      setTasks([...tasks, newTask]);
    } catch (err) {
      console.error("Error adding task:", err);
    }
  };

  const deleteTask = async (id) => {
    try {
      const response = await fetch(`${API_URL}/delete_task`, {
        method: "DELETE",
        mode: "cors",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ taskId: id }),
      });

      if (!response.ok) throw new Error("Failed to delete task");

      setTasks(tasks.filter((task) => task.id !== id));
    } catch (err) {
      console.error("Error deleting task:", err);
    }
  };

  return (
    <div>
      <InputForm onAdd={addTask} />
      <ul className="task-list">
        {tasks.map((task) => (
          <li key={task.id} className="task-item">
            <span>{task.description}</span>
            <button onClick={() => deleteTask(task.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TaskList;
