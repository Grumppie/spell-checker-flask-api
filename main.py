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
    words = word.split(' ')
    res = True
    for word in words:
        if word != spell.correction(word):
            res = False
    response = jsonify(correct=res)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
 
