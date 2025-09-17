import React, { useState } from "react";

const API_URL = "http://127.0.0.1:5001";

function InputForm({ onAdd }) {
  const [input, setInput] = useState("");

  const handleAdd = () => {
    onAdd(input);
    setInput("");
  };

  return (
    <div className="input-section">
      <input
        type="text"
        value={input}
        placeholder="Enter a task..."
        onChange={(e) => setInput(e.target.value)}
      />
      <button onClick={handleAdd}>Add</button>
    </div>
  );
}

export default InputForm;
