from flask import Flask, jsonify, request
from utils import get_smartphones

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
    
@app.route('/smartphones', methods=['GET'])
def view_smartphones():
    price = request.args.get("price")
    
    smartphones = [smartphone for smartphone in get_smartphones() if smartphone.get("price") == price]
    return jsonify(smartphones)

if __name__ == '__main__':
    app.run(debug=True)