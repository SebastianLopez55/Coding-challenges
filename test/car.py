class Car:
    def __init__(self, wheels, doors, motor, ID):
        self.wheels = wheels
        self.doors = doors
        self.motor = motor
        self.ID = ID
        self.cost = wheels * doors + ID

    def turn_on(self, key):
        if self.ID == key:
            print("Car turning ON ....")

        else:
            print('WRONG KEY')

    def car_cost(self):
        return self.cost


Ferrari = Car(4, 2, "V12", 999)

KEY = 999
Ferrari.turn_on(KEY)
print(Ferrari.car_cost())

