# public => variablename
# protected => _variablename
# private => __variablename
# to access private => object._class.__variablename

class MotorCycle:
    numberOfWheels = 2
    _color = "black"
    __yearOfProduction = 2019

class Yamaha(MotorCycle):
    def __init__(self):
        print("Protected attr color:", self._color)