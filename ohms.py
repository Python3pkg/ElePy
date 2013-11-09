#Joe Borg - Ohms - 05/03/2012
from decimal import Decimal

class Ohms(object):
    """
Written to be a very simple calculator; 
construct Ohms with 2 of the 3 required 
parameters to make the calculation, or 
set afterwards using the `set` methods.
    """
    def __init__(self, V=None, I=None, R=None):
            try:
                self.volts = Decimal(V)
            except TypeError:
                self.volts = None
            try:
                self.current = Decimal(I)
            except TypeError:
                self.current = None
            try:
                self.resistance = Decimal(R)
            except TypeError:
                self.resistance = None

    def setVoltage(self, V):
        self.volts = Decimal(V)

    def setCurrent(self, C):
        self.current = Decimal(C)

    def setResistance(self, R):
        self.resistance = Decimal(R)

    def getVoltage(self):
        if not self.volts:
            self.volts = self.current * self.resistance
        print self.volts

    def getCurrent(self):
        if not self.current:
            self.current = self.volts / self.resistance
        print self.current

    def getResistance(self):
        if not self.resistance:
            self.resistance = self.volts / self.current
        print self.resistance
