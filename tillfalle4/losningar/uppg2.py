# Skapa en klass Bil (jag ändrade till Car) som innehåller parametrarna
# reg_plate, owner, color, year_built och som innehåller
# metoden __init__ och metoden print_car_info som printar ut all
# information om bilen på ett snyggt sätt

class Car:
    reg_plate = None
    owner = None
    color = None
    year_built = None

    def __init__(self, reg_plate, owner, color, year_built):
        self.reg_plate = reg_plate
        self.owner = owner
        self.color = color
        self.year_built = year_built

    def print_car_info(self):
        print("The car has registration plate number: " + self.reg_plate)
        print("The car is: " + self.color)
        print("The car is owned by: " + self.owner)
        print("The car is built in: " + str(self.year_built))


my_car = Car("ABC123", "Joakim", "Blue", 1997)
my_car.print_car_info()
