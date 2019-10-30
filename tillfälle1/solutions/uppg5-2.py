# Uppgift 5: Skapa ett program (vowel.py) som tar en bokstav som indata och printar
# Ja! Om bokstaven är en vokal och Nej! Om bokstaven är en konsonant
# Lösningsförslag 2

# Skapar en lista med alla vokaler och lägger i variabeln vokaler
vokaler = ["a", "e", "i", "o", "u", "y", "å", "ä", "ö"]

# Hämtar indata i form av en bokstav och gör den till små bokstäver/gemener (lower case)
# och lägger den i variabeln bokstav
bokstav = input("Skriv en bokstav: ").lower()

# kollar om bokstav finns i listan vokaler med hjälp av funktionen 'in'
if bokstav in vokaler:
    print("Ja!") # Om bokstaven tillhör listan vokaler, printa Ja!
else:
    print("Nej!") # Annars, printa Nej!
