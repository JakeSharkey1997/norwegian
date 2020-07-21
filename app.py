from flask import Flask, escape, request
import random_word


app = Flask(__name__)


@app.route('/')
def hello():
    word_count = request.args.get('word_count', '')
    html = '<form>' \
           'How many words?:  <input name="word_count" value="' + str(word_count) + '"><br>' \
           '<input type="submit">' \
           '</form>'
    translations = get_translation(word_count)
    for translation in translations:
        html += translation[0] + ' --> ' + translation[1] + '<br>'
    return html


def get_translation(word_count):
    if word_count is not '':
        word_count = int(word_count)
        with open('norsk.txt', 'r') as file:
            all_norsk_words = file.readlines()
            all_norsk_words = random_word.remove_syntax_from_list(all_norsk_words)
            norsk_words = random_word.get_norsk_words(word_count * 3, all_norsk_words)
            translator = random_word.Translator()
            return random_word.translate(norsk_words, translator)[:word_count]
    return None

