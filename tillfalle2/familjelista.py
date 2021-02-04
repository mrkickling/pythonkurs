# Vi ber användaren om namn att lägga i en lista
lista = []
namn = input("Säg ett namn: ")

while namn != "done":
    lista.append(namn)
    namn = input("Säg ett till namn: ")

print(lista)
