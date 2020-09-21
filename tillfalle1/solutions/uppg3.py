# Uppgift 4: Skapa ett program (greeting.py) som tar in ett förnamn
# och ett efternamn och åldern och printar ut en hälsning som använder
# sig av den informationen, t.ex. “Hej Förnamn Efternamn, du är 18 år”

# Ber om förnamn och lagrar det i variabeln fornamn (kommer att vara en sträng)
fornamn = input("Förnamn: ")
# Ber om efternamn och lagrar det i variabeln efternamn (kommer att vara en sträng)
efternamn = input("Efternamn: ")
# Ber om ålder och lagrar i age (ok att det är en sträng, då vi bara ska printa det)
age = input("Ålder: ")

print("Hej " + fornamn + " " + efternamn + "! Du är " + age + " år.")
# Går också med print("Hej", fornamn, efternamn, " du är", age, "år.")
