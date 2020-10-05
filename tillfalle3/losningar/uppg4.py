def my_reverse(meddelande):
    resultat = "" # Tom sträng
    antal_bokstaver = len(meddelande)
    for index in range( antal_bokstaver ):
        # Gå igenom varje index för varje bokstav i meddelande
        resultat += meddelande[antal_bokstaver - 1 - index]
    return resultat


print(my_reverse("hejsan"))
