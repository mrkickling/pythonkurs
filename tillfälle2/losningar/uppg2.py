# Addera alla jämna tal från 0 tom 1000 och printa resultatet

# Vi behöver en variabel där vi lagrar summan
sum = 0

for i in range(1001): # Vi går igenom alla tal från 0 till 1000
    if i % 2 == 0: # Om talet är jämnt
        sum = sum + i # Lägg till det på sum

print(sum) # viktigt att print inte är indenterad (hör inte till for-loopen)
