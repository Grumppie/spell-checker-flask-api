from flask import Flask, jsonify, request
from spellchecker import SpellChecker
import json
import os

app = Flask(__name__)

spell = SpellChecker()


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return 'hi'
    word = json.loads(request.data)['Log']
    response = jsonify(correct=spell.correction(word))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
 
