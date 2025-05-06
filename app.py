from flask import Flask, request


app = Flask(__name__)


@app.route("/api/calcs/<value>", methods=["GET"])
def calculate(value):
    try:
        number = int(value)
        if number <= 0:
            abort(404)
    except ValueError:
        abort(400)

    return {}
