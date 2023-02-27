'''class myclass:
    x=5
    
p1=myclass()
print(p1.x)
'''


'''class dormitory:
    def __init__(self,s1,s2):
        self.st1=s1
        self.st2=s2
        
    def __str__(self):
        return f"{self.st1}({self.st2})"
        
p1=dormitory("John","Bred")

print(p1.st1)
print(p1.st2)
print(p1)
'''

'''class dfg:
    def __init__(self,x,y):
        self.x1=x
        self.y1=y
        
    def __str__(self):
        return f"{self.x1}({self.y1})"
    
p=dfg(12,15)

print(p.x1)
print(p.y1)
print(p)
'''


'''
class mc:
    def __init__(self, name, age):
        self.n=name
        self.a=age
        
    def mf1(self):
        print("hello my name is "+ self.n)
        
    def mf2(self,num):
        self.n1=num
        print(self.n1)
        
p1=mc("John",36)
p1.mf1()
p1.mf2(5)
'''

'''
class mc:
    def __init__(self):
       """ self.n=name
        self.a=age"""
    pass
        
    def enters(self):
        self.string=input()
        self.int=input()
    
    def prints(self):
        print(self.string)
        print(self.int)
        
p=mc()
p.enters()
p.prints()
    '''
    
    
'''class mc:
    def __init__(self,name,age):
        self.n=name
        self.a=age
        
    def prints(self):
        print(self.n, self.a)
        
p=mc("John",36)
p.a=40
p.prints()
'''


#inhirites
'''class mc:
    def __init__(self,fname,lname):
        self.f=fname
        self.l=lname
        
    def prints(self):
        print(self.f, self.l)
        
class Student(mc):
    def __init__(self,name,surname):
        self.n=name
        self.s=surname
    """ self.string=input()"""
    
    def prints1(self):
        print(self.n, self.s)
        

p=mc("Mike","Olsen")
p.prints()
p1=Student("Olsen","Mike")
p1.prints1()
'''




'''
class Parent:
    def __init__(self, fname,lname):
        self.f=fname
        self.l=lname
        
    def prints(self):
        print(self.f, self.l)
        
class Student(Parent):
    def __init__(self,name,surname):
        self.n=name
        self.s=surname
        Parent.__init__(self,name,surname)
        
p=Student("Olsen","Mikey")
p.prints()
'''


'''class Parent :
    def __init__(self,fname,lname):
        self.f=fname
        self.l=lname
        
    def prints(self):
        print(self.f, self.l)
        
class Student(Parent):
    def __init__(self,name,surname,year):
        super().__init__(name,surname)
        self.graduationyear=year


p=Student("Olsen","Mikey",2019)
print(p.graduationyear)
print(p.f, p.l)
'''


'''
class Prime:
    def __init__(self, a):
        self.a = a

    def filter_prime(y):
        y=[]
        for i in range(len(a)):
           if a[i] == 1:
                continue
           t = True
           for j in range(2, a[i]):
                if a[i] % j == 0:
                   t = False
                   break
           if t == True:
                y.append(a[i])
        print(y)

a = [int(x) for x in input().split()]
#print(a)
p = Prime(a)
p.filter_prime()
'''


"""def is_prime(x):
    for i in range(2, int(x / 2) + 1):
        if x % i == 0:
            return 0
    return 1

filter = lambda a: is_prime(a)

n = int(input("Write some number\nn="))
prime = filter(n)

if prime > 0:
    print(f"{n} is prime number")
else:
    print(f"{n} is not prime number")
"""



class Prine:
    def __init__(self):
        pass
    
    