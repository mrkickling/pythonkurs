# Skapa ett gissningsspel
# 1. Programmet väljer ett slumptal (hemligt tal)
# 2. Användaren gissar vilket talet är
# 3. Om gissningen är fel så printar programmet "gissa högre" eller "gissa lägre"
#       Och upprepar sedan steg 2 till 3 tills gissningen är korrekt
# 4. Printa "Rätt svar!" om gissningen är korrekt

import random # Vi importerar modulen random för att kunna skapa slumptal

# Vi skapar ett slumptal mellan 0 och 100 och lagrar i en variabel
slumptal = random.randrange(100)
# Sedan ber vi användaren om en gissning
gissning = int(input("Gissa vilket talet är: "))


while gissning is not slumptal:
    if gissning > slumptal:
        print("Gissa lägre! ")
    else:
        print("Gissa högre! ")
        
    gissning = int(input("Gissa igen: ")) # Vi ber om nya gissningar så länge gissningen är fel

print("Du gissade rätt. Grattis!")
