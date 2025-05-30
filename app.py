from flask import Flask, request, jsonify, abort


app = Flask(__name__)


@app.route("/api/calcs/<value>", methods=["GET"])
def calculate(value):
    try:
        number = int(value)
        if number <= 0:
            abort(404)
    except ValueError:
        abort(400)
    result = {
        "dec": number - 1,
        "hex": hex (number)
    }
    return jsonify(result)
