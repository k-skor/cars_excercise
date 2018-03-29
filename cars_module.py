import php

class GasCar(php.BaseCar):
    def __init__(self):
        self.sound = "brrrum"

    def drive(self):
        return self.sound

    def __add__(self, other):
        if type(other) is GasCar or type(other) is DieselCar:
            raise CarAccident()

class DieselCar(php.BaseCar):
    def __init__(self):
        self.sound = "pyr pyr pyr"

    def drive(self):
        return self.sound

    def __add__(self, other):
        if type(other) is GasCar or type(other) is DieselCar:
            raise CarAccident()

class CarAccident(Exception):
    def __init__(self):
        super(CarAccident, self).__init__("Crash!")

"""
gasCar = GasCar()
dieselCar = DieselCar()
print("{} {}".format(gasCar.drive(), dieselCar.drive()))
gasCar2 = GasCar()
gasCar2 + gasCar
print("{}".format(gasCar2.drive()))
try:
    dieselCar + gasCar
except CarAccident as e:
    print("Exception: {}".format(e))
"""