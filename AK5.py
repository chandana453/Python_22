class Inputoutstring(object):
    def _init_ (self):
       self.s=""
    def getstring(self):
        self.s=input()
    def printstring(self):
        print(self.s.upper())
strobj=Inputoutstring()
strobj.getstring()
strobj.printstring()