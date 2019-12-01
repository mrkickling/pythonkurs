class Land:
    def __init__(self, namn, befolkning):
        self.namn = namn
        self.befolkning = befolkning

    def printBefolkning(self):
        print(self.befolkning)

    def printNamn(self):
        print(self.namn)

sverige = Land("Sverige", 10000000)
norge = Land("Norge", 3000000)

sverige.printNamn()
norge.printBefolkning()
