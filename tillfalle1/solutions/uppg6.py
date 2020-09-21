# Skapa ett program (append.py) som tar in tre heltal som indata 
# och lägger till var och ett av dom i en lista om dom är större än 10

tal1 = int(input("Tal1: "))
tal2 = int(input("Tal2: "))
tal3 = int(input("Tal3: "))

lista = []

if tal1 > 10:
    lista.append(tal1)
if tal2 > 10:
    lista.append(tal2)
if tal3 > 10:
    lista.append(tal3)

print(lista)