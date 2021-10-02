from flask import Flask, request, jsonify
from flask_cors import CORS
from data.data import data

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({'data': data, 'message': 'Success'}), 200

@app.route('/star_single')
def single_planet():
    star_data = []
    star_name = request.args.get('name')
    for each_item in data:
        if each_item['name'] == star_name:
            star_data.append(each_item)

    return jsonify({'data': star_data, 'message': 'Success'}), 200

if __name__ == '__main__':
    app.run(debug=True)