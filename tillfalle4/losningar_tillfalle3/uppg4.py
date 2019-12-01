# En funktion som hittar maxvärdet i en lista

def my_max(lista):
    max = -float("inf") # det minsta talet som finns
    for heltal in lista:
        if heltal > max:
            max = heltal
    return max


print(my_max([100000, 2, 3000000, 4, 5, -1000]))
