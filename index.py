import json
from difflib import SequenceMatcher as sm

data = json.load(open("./data.json"))


def find_definition(word):
    if word in data:
        return data[word]
    else:
        return "Word does not exist."




word = input("Find a word:")
word = word.lower()
print(sm(None, "rain", word).ratio())


print(find_definition(word))