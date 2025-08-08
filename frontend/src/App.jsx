
import PowCalculator from './components/PowCalculator';
import FactorialCalculator from './components/FactorialCalculator';
import FibonacciCalculator from './components/FibonacciCalculator';
import './App.css';

function App() {
  return (
    <div className="center-wrapper">
      <div className="main-container">
        <h1 className="main-title">Math Service Frontend</h1>
        <div className="card-grid">
        <div className="card"><FibonacciCalculator /></div>
        <div className="card"><FactorialCalculator /></div>
        <div className="card"><PowCalculator /></div>
        </div>
      </div>
    </div>
  );
}

export default App
