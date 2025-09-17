import React from "react";
import "./App.css";
import TaskList from "./Components/TaskList";

function App() {
  return (
    <div className="app">
      <h1>Todo List</h1>
      <TaskList />
    </div>
  );
}

export default App;
