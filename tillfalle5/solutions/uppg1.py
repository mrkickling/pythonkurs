# Gör en funktion som tar in ett namn/text (sträng) och returnerar strängen i rövarspråket
# (hej => hohejoj, erik => erorikok)  och testa den med några strängar

def rovarsprak(text):
    text = text.lower() # Gör allt till lowercase för enklare program
    konsonanter = "bcdfghjklmnpqrstvwxz"
    result = "" # vår resultat-sträng
    for letter in text: # gå igenom alla bokstäver i indata-strängen (i ordning)
        if letter in konsonanter: # Om bokstaven är en konsonant, lägg in bokstav + o + bokstav
            result += letter + "o" + letter
        else: # Annars lägg till som vanligt i resultatsträngen
            result += letter

    return result


print(rovarsprak("test")) # borde printa ut totesostot
print(rovarsprak("mitt namn är erik")) # borde printa ut momitotot nonamomnon äror erorikok
