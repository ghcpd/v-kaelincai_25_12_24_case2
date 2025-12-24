"""
Flask application for e-commerce order filtering with date picker.
This simulates a Safari-specific CSS bug with date input styling.
"""
from flask import Flask, render_template, jsonify, request
from datetime import datetime, timedelta
import json

app = Flask(__name__)

# Sample order data
SAMPLE_ORDERS = [
    {
        "id": "ORD-001",
        "date": "2025-12-01",
        "customer": "John Doe",
        "amount": 150.00,
        "status": "completed"
    },
    {
        "id": "ORD-002",
        "date": "2025-12-05",
        "customer": "Jane Smith",
        "amount": 299.99,
        "status": "pending"
    },
    {
        "id": "ORD-003",
        "date": "2025-12-08",
        "customer": "Bob Johnson",
        "amount": 75.50,
        "status": "completed"
    },
    {
        "id": "ORD-004",
        "date": "2025-12-10",
        "customer": "Alice Brown",
        "amount": 425.00,
        "status": "shipped"
    },
    {
        "id": "ORD-005",
        "date": "2025-12-11",
        "customer": "Charlie Wilson",
        "amount": 189.99,
        "status": "completed"
    }
]


@app.route('/')
def index():
    """Render the main order filtering page."""
    return render_template('index.html')


@app.route('/api/orders', methods=['GET'])
def get_orders():
    """
    Get orders, optionally filtered by date range.
    Query params: start_date, end_date (YYYY-MM-DD format)
    """
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    
    filtered_orders = SAMPLE_ORDERS.copy()
    
    if start_date:
        try:
            start = datetime.strptime(start_date, '%Y-%m-%d')
            filtered_orders = [
                order for order in filtered_orders
                if datetime.strptime(order['date'], '%Y-%m-%d') >= start
            ]
        except ValueError:
            return jsonify({"error": "Invalid start_date format"}), 400
    
    if end_date:
        try:
            end = datetime.strptime(end_date, '%Y-%m-%d')
            filtered_orders = [
                order for order in filtered_orders
                if datetime.strptime(order['date'], '%Y-%m-%d') <= end
            ]
        except ValueError:
            return jsonify({"error": "Invalid end_date format"}), 400
    
    return jsonify({
        "orders": filtered_orders,
        "count": len(filtered_orders)
    })


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "ok"})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
