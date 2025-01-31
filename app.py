from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# This would typically come from a database
PRODUCTS = {
    '1': {'name': 'Premium Widget', 'actual_price': 99.99},
    '2': {'name': 'Super Gadget', 'actual_price': 149.99},
}

@app.route('/')
def index():
    return render_template('index.html', products=PRODUCTS)

@app.route('/purchase', methods=['POST'])
def purchase():
    product_id = request.form.get('product_id')
    # VULNERABLE: Price is accepted from client side without validation
    price = float(request.form.get('price', 0))
    quantity = int(request.form.get('quantity', 1))
    
    if product_id not in PRODUCTS:
        return jsonify({'error': 'Invalid product'}), 400
    
    # Calculate total (vulnerable to price manipulation)
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