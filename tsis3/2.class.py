class Shape:
       
    def Area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
        self.l = length
        
    def Area(self):
        print(self.l*self.l)

len = int(input())
p1 = Shape()
p2 = Square(len)
print(p1.Area())
p2.Area()

