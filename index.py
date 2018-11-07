import json
from difflib import SequenceMatcher as sm
from difflib import get_close_matches as gcm

data = json.load(open("./data.json"))


def find_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(gcm(word, data, n=1)) > 0:
        suggestion = gcm(word, data, n=1)
        response = input("Did you mean %s? (Y/N) " % suggestion[0])
        if response.lower() == "y" :
            return data[suggestion[0]]
        elif response.lower() == "n":
            return "I don't know what word you are looking for. Please try again."
    else:
        return "The word doesn't exist. Please double check it."
    


def get_word():
    return input("Enter a word: ")


def run_program():
    word = get_word()
    response = find_definition(word)
    if type(response) is list:
        for index, definition in enumerate(response):
            print("%s. %s" % (index + 1, definition))
    else:
        print(response)
            
run_program()