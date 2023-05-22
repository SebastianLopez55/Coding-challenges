from car import Car


def test_car_cost():
    car = Car(4, 2, "V12", 999)
    assert car.car_cost() == 1007
