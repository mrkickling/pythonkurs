# Uppgift 5: Skapa ett program (vowel.py) som tar en bokstav som indata och printar
# Ja! Om bokstaven är en vokal och Nej! Om bokstaven är en konsonant
# Lösningsförslag 1

# Hämtar indata i form av en bokstav och gör den till små bokstäver/gemener (lower case)
bokstav = input("Skriv en bokstav: ").lower()

# Jämför bokstaven med alla vokaler
if bokstav == "a":
    print("Ja!")
elif bokstav == "e": # Om bokstaven ej är "a", kolla om den är "e"
    print("Ja!")
elif bokstav == "i": # Om bokstaven ej är "a" eller "e", kolla om den är "i"
    print("Ja!")
elif bokstav == "o": # Om bokstaven ej är "a" eller "e" eller "i", kolla om den är "o"
    print("Ja!")
elif bokstav == "u": # osv
    print("Ja!")
elif bokstav == "y": # osv
    print("Ja!")
elif bokstav == "å": # osv
    print("Ja!")
elif bokstav == "ä": # osv
    print("Ja!")
elif bokstav == "ö": # osv
    print("Ja!")
else:                # om bokstaven ej är någon av vokalerna så måste den vara en konsonant
    print("Nej!")
