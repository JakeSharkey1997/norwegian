import random
from googletrans import Translator


def random_word_from_list(all_norsk_words):
    return random.choice(all_norsk_words)


def get_word_count_input():
    return int(input("How many words do you want to see? "))


def get_norsk_words(counter, all_norsk_words):
    list_of_words = []
    while counter is not 0:
        list_of_words.append(random_word_from_list(all_norsk_words))
        counter -= 1
    return list_of_words


def remove_syntax_from_list(all_norsk_words):
    words_updated = []
    for word in all_norsk_words:
        words_updated.append(word[:-1])
    return words_updated


def translate(norsk_words, translator):
    list_of_translated_words = []
    translations = translator.translate(norsk_words, src='no', dest='en')
    for translation in translations:
        if translation.origin != translation.text:
            list_of_translated_words.append([translation.origin, translation.text])
    return list_of_translated_words


def main():
    with open('norsk.txt', 'r') as file:
        all_norsk_words = file.readlines()
        all_norsk_words = remove_syntax_from_list(all_norsk_words)
        word_count = get_word_count_input()
        norsk_words = get_norsk_words(word_count * 3, all_norsk_words)
        translator = Translator()
        translations = translate(norsk_words, translator)
        for translation in translations[:word_count]:
            print(translation[0] + " --> " + translation[1])


if __name__ == "__main__":
    main()
