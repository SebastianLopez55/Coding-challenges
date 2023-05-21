


class Motor:

    def __init__(self, motorType):
        self.motorType = motorType

    def change_oil(self, liters):

        # This motor needs 2L of Oil
        if liters < 2:
            print('Not enough oil')
        else:
            print('Remember just to pour 2 liters!!')

class Car(Motor):
    def __init__(self, wheels, doors, motor, ID):
        self.wheels = wheels
        self.doors = doors
        self.motor = motor
        self.ID = ID
        super().__init__(motor)

    def turn_on(self, key):
        if self.ID == key:
            print("Car turning ON ....")

        else:
            print('WRONG KEY')


Ferrari = Car(4, 2, "V12", 999)

KEY = 999
Ferrari.turn_on(KEY)
Ferrari.change_oil(3)


def test_car_turn_on():
    key = 999
    ferrari = Car(4, 2, "V12", key)
    assert ferrari.turn_on(key) == "Car turning ON ...."
    assert ferrari.turn_on(123) == "WRONG KEY"


def test_motor_change_oil():
    motor = Motor("V12")
    assert motor.change_oil(1) == "Not enough oil"
    assert motor.change_oil(3) == "Remember just to pour 2 liters!!"

