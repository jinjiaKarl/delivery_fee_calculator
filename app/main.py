from flask import Flask
from flask import request, jsonify
from calculator import SimpleCalculator, Strategy
import logging

logging.basicConfig(format='%(asctime)s,%(msecs)03d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG)
app = Flask(__name__)

@app.get("/")
def delivery_get():
    return "<p>Delivery Fee Calculator!</p>"


@app.post("/")
def delivery_post():
    body = request.get_json()
    fee = Strategy(SimpleCalculator()).get_results(app, body)
    if fee == -1:
        app.logger.error("Invalid input")
        return jsonify({"error": "Invalid input"}), 400
    return jsonify({"delivery_fee": fee})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)