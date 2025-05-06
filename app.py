from flask import Flask, request


app = Flask(__name__)


@app.route("/api/calcs/<value>", methods=["GET"])
def method_name():
    return {}
