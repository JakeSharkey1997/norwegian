import random
from googletrans import Translator


def random_word(updated_list):
    picked_word = random.choice(updated_list)
    return picked_word


def generate_words():
    number_of_words_str = input("How many words do you want to see? ")
    counter = int(number_of_words_str)
    return counter


def chosen_words(counter, updated_list):
    list_of_words = []
    while counter is not 0:
        list_of_words.append(random_word(updated_list))
        counter -= 1
    return list_of_words


def remove_syntax(words):
    words_updated = []
    for word in words:
        words_updated.append(word[:-1])
    return words_updated


def translate(norsk_words, translator):
    translation_list = []
    translations = translator.translate(norsk_words, src='no', dest='en')
    for translation in translations:
        if translation.origin != translation.text:
            translation_list.append([translation.origin, translation.text])
    return translation_list


if __name__ == "__main__":
    with open('norsk.txt', 'r') as file:
        words = file.readlines()
        updated_list = remove_syntax(words)
        number = generate_words()
        norsk_words = chosen_words(number*3, updated_list)
        translator = Translator()
        translation_list = translate(norsk_words, translator)
        for translation in translation_list[:number]:
            print(translation[0] + " --> " + translation[1])
