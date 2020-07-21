from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/')
def hello():
    word_count = request.args.get('word_count', '')
    return '<form>' \
           'How many words?:  <input name="word_count" value="'+word_count+'"><br>' \
           '<input type="submit">' \
           '</form>'