# Uppgift 6: Skapa ett program (max.py) som tar in tre tal som indata
# och printar ut det största av de tre värdena
# Lösningsförslag (ej enda lösningen)

# Hämtar tre tal som indata, gör om dessa till heltal
# och sparar dom i en varsin variabel
a = int(input("Skriv ett första tal: "))
b = int(input("Skriv ett andra tal: "))
c = int(input("Skriv ett tredje tal: "))

# Jämför talen
if (a > b and a > c): # Om a är större än b, och a är större än c
    print(a)    # a är störst
elif (b > a and b > c): # annars, om b är större än a och b är större än c
    print(b)    # b är störst
else:
    print(c) # Annars är c störst
