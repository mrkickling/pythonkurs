# Uppgift 2: Skapa ett program (power.py) som tar två siffror som
# indata och printar ut det första talet upphöjt till det andra
# Lösningsförslag (såklart inte enda sättet!)

# ber om den första siffran, gör om till decimaltal och sparar i variabel a
# float används istället för int, men int är också okej!
a = float(input("Skriv en siffra "))

# ber om den andra siffran, gör om till decimaltal och sparar i variabel b
b = float(input("Skriv en till siffra "))

# skapar en variabel (result) som jag säger är a upphöjt i b
result = a ** b

# printar resultatet
print(result)
