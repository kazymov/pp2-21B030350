class Shape:
    def __init__(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, lenght, width):
        self.l=lenght
        self.w=width
        
    def Area(self):
        print(self.l*self.w)
        
len=int(input())
wid=int(input())
p1=Rectangle(len,wid)
p1.Area()