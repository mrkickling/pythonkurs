# Skriver namn på ny rad i filen "namnlista.txt"
f = open("namnlista.txt","a")
f_name = input("Förnamn: ")
l_name = input("Efternamn: ")
age = input("Ålder: ")

# Kommer du ihåg vad \n representerar för något?
f.write(f_name + " " + l_name + ": " + age + "\n")
f.close()

# Hur kan vi fråga användaren 3 gånger utan att kopiera och klista in all kod tre gånger?
