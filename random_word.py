import random
from googletrans import Translator


def random_word_from_list(updated_list):
    picked_word = random.choice(updated_list)
    return picked_word


def inputted_number_of_words():
    number_of_words_str = input("How many words do you want to see? ")
    counter = int(number_of_words_str)
    return counter


def list_of_norsk_words(counter, updated_list):
    list_of_words = []
    while counter is not 0:
        list_of_words.append(random_word_from_list(updated_list))
        counter -= 1
    return list_of_words


def remove_syntax_from_file(words_file):
    words_updated = []
    for word in words_file:
        words_updated.append(word[:-1])
    return words_updated


def translate(norsk_words, translator):
    list_of_translated_words = []
    translations = translator.translate(norsk_words, src='no', dest='en')
    for translation in translations:
        if translation.origin != translation.text:
            list_of_translated_words.append([translation.origin, translation.text])
    return list_of_translated_words


if __name__ == "__main__":
    with open('norsk.txt', 'r') as file:
        words_file = file.readlines()
        updated_list = remove_syntax_from_file(words_file)
        number = inputted_number_of_words()
        norsk_words = list_of_norsk_words(number * 3, updated_list)
        translator = Translator()
        translation_list = translate(norsk_words, translator)
        for words in translation_list[:number]:
            print(words[0] + " --> " + words[1])
