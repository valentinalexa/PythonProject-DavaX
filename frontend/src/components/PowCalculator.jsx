// PowCalculator.jsx
import React, { useState } from 'react';

const PowCalculator = () => {
  const [x, setX] = useState('');
  const [y, setY] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setResult(null);
    try {
      const response = await fetch('http://localhost:5000/pow', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ x: parseFloat(x), y: parseFloat(y) })
      });
      const data = await response.json();
      if (response.ok) {
        setResult(data.result);
      } else {
        setError(data.error || 'Error');
      }
    } catch (err) {
      setError('Network error');
    }
  };

  return (
    <div>
      <h2>Power Calculator</h2>
      <form onSubmit={handleSubmit}>
        <input type="number" value={x} onChange={e => setX(e.target.value)} placeholder="x" required />
        <input type="number" value={y} onChange={e => setY(e.target.value)} placeholder="y" required />
        <button type="submit">Calculate</button>
      </form>
      {result !== null && <div>Result: {result}</div>}
      {error && <div style={{color:'red'}}>{JSON.stringify(error)}</div>}
    </div>
  );
};

export default PowCalculator;
