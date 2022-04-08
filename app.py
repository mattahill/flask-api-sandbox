from flask import Flask, Response
import json
from apiflask import APIFlask


# app = Flask(__name__)
app = APIFlask(__name__, enable_openapi=False)
app.config['SPEC_FORMAT'] = 'yaml'
app.config['DESCRIPTION'] = 'This is a test api sandbox utilizing api flask to generate documentation'


@app.route("/")
def index():
    """index
    this is the index
    """
    return '<p><a href="/200">200 response</a></p><p><a href="/404">404 response</a></p>'


@app.route("/200")
@app.doc(responses=[200])
def hello_world():
    """hello world
    this is the hello world route
    """
    return Response(json.dumps({"hello": "world"}), 200, mimetype="application/json")


@app.route("/404")
@app.doc(responses=[404])
def return_404():
    """404 page
    this is the 404 page
    """
    return Response(json.dumps({"not": "found"}), 400, mimetype="application/json")
