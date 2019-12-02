# En funktion som kontrollerar om en sträng är ett palindrom
def my_reverse(meddelande):
    resultat = "" # Tom sträng
    antal_bokstaver = len(meddelande)
    for index in range( antal_bokstaver ):
        # Gå igenom varje index för varje bokstav i meddelande
        resultat += meddelande[antal_bokstaver - 1 - index]
    return resultat

def is_palindrom(meddelande):
    if meddelande == my_reverse(meddelande):
        return True
    else:
        return False

print(is_palindrom("hejsan"))
print(is_palindrom("fallaf"))
