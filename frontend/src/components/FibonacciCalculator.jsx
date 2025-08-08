// FibonacciCalculator.jsx
import React, { useState } from 'react';

const FibonacciCalculator = () => {
  const [n, setN] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setResult(null);
    try {
      const response = await fetch('http://localhost:5000/fibonacci', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ n: parseInt(n) })
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
      <h2>Fibonacci Calculator</h2>
      <form onSubmit={handleSubmit}>
        <input type="number" value={n} onChange={e => setN(e.target.value)} placeholder="n" required />
        <button type="submit">Calculate</button>
      </form>
      {result !== null && <div>Result: {result}</div>}
      {error && <div style={{color:'red'}}>{JSON.stringify(error)}</div>}
    </div>
  );
};

export default FibonacciCalculator;
