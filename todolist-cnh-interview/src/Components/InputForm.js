import React, { useState } from "react";

// Backend API URL (not directly used in this component, 
// but can be useful for consistency if expanded later)
const API_URL = "http://127.0.0.1:5001";

// InputForm component handles capturing user input for new tasks
// Props:
//   onAdd - callback function passed from parent (adds a task to the list)
function InputForm({ onAdd }) {
  // Local state for the text input field
  const [input, setInput] = useState("");

  // Triggered when "Add" button is clicked
  // Calls the parent's onAdd function with the input value
  // and clears the input field
  const handleAdd = () => {
    onAdd(input);
    setInput("");
  };

  return (
    <div className="input-section">
      {/* Text input field for task description */}
      <input
        type="text"
        value={input}
        placeholder="Enter a task..."
        onChange={(e) => setInput(e.target.value)} // Update state as user types
      />

      {/* Add button calls handleAdd when clicked */}
      <button onClick={handleAdd}>Add</button>
    </div>
  );
}

export default InputForm;
