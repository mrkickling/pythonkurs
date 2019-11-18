# Låt säga att vi har en lista:
list1 = [-10, -8, -5, 1, 2, 3, 4, 5, 6, 7, 8]
pos_list = []

# Och vi vill ta bort alla tal i listan som är negativa
for element in list1:
    if element > 0:
        pos_list.append(element) # ny lista med alla positiva element

print(pos_list)
