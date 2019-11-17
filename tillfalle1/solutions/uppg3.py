# Uppgift 3: Skapa ett program (even.py) som tar in ett heltal (int) och
# som printar Ja! om talet är jämnt och Nej! om talet är udda. Tips: modulo (%)
# Lösningsförslag (såklart inte enda sättet!)

# ber om heltalet, gör om till int och sparar i variabeln heltal
heltal = int(input("Skriv in ett heltal "))

# Om heltal modulo 2 är 0 så är heltal delbart i 2
if heltal % 2 == 0:
    print("Ja!")
else:
    print("Nej!")
