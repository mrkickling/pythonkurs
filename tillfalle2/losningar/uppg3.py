# Gör en nedräknare för en raket
# 10... 9... 8... 7... ... osv ... LIFT OFF!
# Använd time.sleep!

import time # Vi importerar modulen time

for i in range(10): # Vi går igenom alla tal från 0 till 10
    print(10 - i) # Vi printar 10 - i, vilket kommer bli 10, 9, 8, osv...
    time.sleep(1) # Vi "pausar" programmet i en sekund

print("LIFT OFF!") # När loopen är färdig så printas "LIFT OFF"
