from flask import Flask, request, jsonify
from flask_cors import CORS
from pydantic import ValidationError
from app.models import PowRequest, FactorialRequest, FibonacciRequest, OperationResult
from app.controller import pow_operation, factorial_operation, fibonacci_operation

app = Flask(__name__)
CORS(app)

@app.route('/pow', methods=['POST'])
def pow_route():
    try:
        data = PowRequest(**request.json)
        result = pow_operation(data.x, data.y)
        return jsonify(OperationResult(result=result).dict())
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400

@app.route('/factorial', methods=['POST'])
def factorial_route():
    try:
        data = FactorialRequest(**request.json)
        result = factorial_operation(data.n)
        return jsonify(OperationResult(result=result).dict())
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400

@app.route('/fibonacci', methods=['POST'])
def fibonacci_route():
    try:
        data = FibonacciRequest(**request.json)
        result = fibonacci_operation(data.n)
        return jsonify(OperationResult(result=result).dict())
    except ValidationError as e:
        return jsonify({'error': e.errors()}), 400

if __name__ == '__main__':
    app.run(debug=True)
