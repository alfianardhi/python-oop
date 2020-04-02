"""
python can perform multiplw ineritance
"""
class Instruments:
    numberMajorKeys=12

class StringInstruments(Instruments):
    typeOfWood = "Tone Wood"

class ElectricInstruments():
    brand = "Yamaha"


class Guitar(StringInstruments, ElectricInstruments):
    def __init__(self):
        self.numberOfStrings = 6
        print("Guitar consits of {} strings. It's made of {} and it can play {} key and guitar's brand is {}".format(self.numberOfStrings, self.typeOfWood, self.numberMajorKeys, self.brand))