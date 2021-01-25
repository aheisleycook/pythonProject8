""":type
this class holds the methods
"""
class Temperature:
    """:type"""

    def __init__(self):
        self.temps = []

    def setTemperatureread(self, p) -> object:
        self.temp = p
        self.temps.append(self.temp)

    def getmaxTemp(self):
        self.curtemp = 0
        self.maxTemp = 0
        for tp in self.temps:
           self.curtemp = tp
           if self.curtemp > tp:
               self.maxTemp = self.curtemp
        return self.maxTemp



