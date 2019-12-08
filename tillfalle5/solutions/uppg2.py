# Skapa en dictionary som innehåller några engelska ord som nyckel
# och deras svenska översättningar som värden, skapa sedan en funktion
# som tar in ett engelskt ord och returnerar det svenska ordet.
# Om översättningen inte finns så returnera “Sorry, not found”

english_to_swedish = {
    "hello": "hej",
    "hi": "hej",
    "english" : "engelsk",
    "frog" : "groda"
}

def translate(word):
    if word in english_to_swedish:
        return english_to_swedish[word]
    else:
        return "Sorry, word not found"

word_input = input("Translate word to swedish: ")
print(translate(word_input))
