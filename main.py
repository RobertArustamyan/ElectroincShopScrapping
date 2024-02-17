from seaching_in_files import sorting_result
import asyncio
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def test():
    return "TEST"

@app.route('/getData',methods=['POST'])
def search_and_sort():
    try:
        data = request.get_json()
        category = data.get('category')
        item_name = data.get('item_name')
        min_price = float(data.get('min_price', 0))
        max_price = float(data.get('max_price', float('inf')))

        result = asyncio.run(sorting_result(category, item_name, min_price, max_price))

        sort_method = data.get('price')

        if sort_method == 'asc':
            sorted_result = sorted(result, key=lambda x: x['price'])
            return jsonify(sorted_result), 200
        elif sort_method == 'desc':
            sorted_result = sorted(result, key=lambda x: x['price'], reverse=True)
            return jsonify(sorted_result), 200

        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True,port=3050,host="0.0.0.0")