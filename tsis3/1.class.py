class Mc:
    def __init__(self):
        pass
    def getstring(self):
        self.string=(input())
        
    def printstring(self): 
        print(self.string.upper())
        
p=Mc()
p.getstring()
p.printstring()
