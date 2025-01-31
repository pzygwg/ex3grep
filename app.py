from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# This would typically come from a database
PRODUCTS = {
    '1': {'name': 'Premium Widget', 'actual_price': 99.99},
    '2': {'name': 'Super Gadget', 'actual_price': 149.99},
}

def validate_price(price_str):
    """Validate price format and range"""
    if not price_str or not isinstance(price_str, str):
        return None
    # Check if price matches valid format (positive number with up to 2 decimal places)
    if not re.match(r'^\d+(\.\d{1,2})?$', price_str):
        return None
    price = float(price_str)
    # Basic range validation
    if price < 0 or price > 10000:  # Reasonable price range
        return None
    return price

def validate_quantity(qty_str):
    """Validate quantity format and range"""
    if not qty_str or not isinstance(qty_str, str):
        return None
    if not qty_str.isdigit():
        return None
    qty = int(qty_str)
    if qty < 1 or qty > 100:  # Reasonable quantity range
        return None
    return qty

@app.route('/')
def index():
    return render_template('index.html', products=PRODUCTS)

@app.route('/purchase', methods=['POST'])
def purchase():
    product_id = request.form.get('product_id')
    price_str = request.form.get('price', '0')
    qty_str = request.form.get('quantity', '1')
    
    # Input validation
    price = validate_price(price_str)
    quantity = validate_quantity(qty_str)
    
    if price is None or quantity is None:
        return jsonify({'error': 'Invalid input parameters'}), 400
    
    if product_id not in PRODUCTS:
        return jsonify({'error': 'Invalid product'}), 400
    
    # The vulnerability is still here - we validate the format but don't check
    # against the actual price in PRODUCTS
    total = price * quantity
    
    # Process purchase (simplified)
    return jsonify({
        'success': True,
        'message': f'Purchase successful! Total paid: ${total:.2f}',
        'product': PRODUCTS[product_id]['name'],
        'quantity': quantity,
        'total': total
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000) 