# Skriver namn på ny rad i filen "namnlista.txt"
def writeToFile(fname, lname, age):
    f = open("namnlista.txt","a")
    f.write(fname + " " + lname + ": " + age + "\n")
    f.close()
    # Behöver ej returna något, vi vill bara skriva till filen

f_name = input("Förnamn: ")
l_name = input("Efternamn: ")
age = input("Ålder: ")

writeToFile(f_name, l_name, age)

# Hur kan vi fråga användaren 3 gånger utan att kopiera och klista in all kod tre gånger?
