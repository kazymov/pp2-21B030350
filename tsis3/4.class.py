class Point:
    def __init__(self,pointx,pointy):
        self.x=pointx
        self.y=pointy
        
    def show(self):
        print(self.x, self.y)
        
    def move(self):
        x1=int(input())
        y1=int(input())
        self.x=x1
        self.y=y1
        
    def distance(self):
        print(((self.x*self.x)+(self.y*self.y))**0.5)
     
        
cx=int(input())
cy=int(input())
p=Point(cx,cy)
p.show()
p.move()
p.distance()

        