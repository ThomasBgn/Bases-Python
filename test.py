import random

quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", "On doit pouvoir choisir entre s'écouter parler et se faire entendre."]
characters = ["Alvin et les Chipmunks", "Babar", "Betty boop", "Calimero", "Casper", "Le chat potté", "Kirikou"]

def get_random_item(object_list):
    rand_numb = random.randint(0, len(object_list) - 1)
    item = object_list[rand_numb] # get a quote from a list
    return item # return the item

def capitalize(lists):
    for list in lists: 
        return list.capitalize()

def message(character, quote):
    capitalize(character)
    capitalize(quote)
    return "{} a dit : {}".format(character, quote)

user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')

while user_answer != "B":
    print(message(get_random_item(characters), get_random_item(quotes)))
    user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')
