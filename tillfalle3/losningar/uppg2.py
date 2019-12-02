# Skriver namn på ny rad i filen "namnlista.txt"
f = open("namnlista.txt","a")
f_name = input("Förnamn: ")
l_name = input("Efternamn: ")
age = input("Ålder: ")

# Kommer du ihåg vad \n representerar för något?
f.write(f_name + " " + l_name + ": " + age + "\n")
f.close()
