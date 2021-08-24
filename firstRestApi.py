import json

from flask import Flask, jsonify

certification = [{'name': "CDL", 'cost': "200$", 'provider': "Google", 'id': "0"},
                 {'name': "AZ-900", 'cost': "99$", 'provider': "MS", 'id': "1"}
                 ]

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome Arvind"


json_obj = json.dumps(certification, indent =4)


@app.route("/cert", methods=['GET'])
def get():
    return json_obj


@app.route("/cert/<int:cert_id>", methods=['GET'])
def get_cert(cert_id):
    return jsonify({'cert': certification[cert_id]})


@app.route("/cert", methods=['POST'])
def create():
    cert = {'name': "AWS", 'cost': "99$", 'provider': "AWS", 'id': "2"}
    certification.append(cert)
    return jsonify({'Created': cert})


if __name__ == "__main__":
    app.run(debug=True)



