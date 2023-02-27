#python- iterators
#An iterator - is an object that can be iterated upon, meaning that you can traverse through all the values.


"""#1
mytuple=("asd","1","dsa","2")
myit=iter(mytuple)

print(next(myit), next(myit))#-asd 1
print(next(myit))#-1
"""

"""#2
mystr="asdfgh"
myit=iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))"""

"""#3
class myclass:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        x=self.a
        self.a+=1
        return x
    
mycl=myclass()
myiter=iter(mycl)
    
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
"""

"""#4-prevent the iteration
class myclass:
    def __iter__(self):
        self.a=1
        return self
    
    def __next__(self):
        if self.a <=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
        
mycl=myclass()
myiter=iter(mycl)

for x in myiter:
    print(x)"""
    
    
# generates:


"""#1
def mygenerator():
    yield 1
    yield 2
    yield 3
    
for value in mygenerator():
    print(value)
            """
    


"""def mygenerator():
    yield 1
    yield 2
    yield 3
    
x=mygenerator()

print(next(x))
print(next(x))
print(next(x))"""


"""def fib(limit):
     
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1
 
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b
 
# Create a generator object
x = fib(5)

for i in fib(5):
    print(i)
"""


# date-A date in Python is not a data type of its own, but we can import a module named "datetime" to work with dates as date objects.

"""#1
import datetime
x=datetime.datetime.now()
print(x) 
"""#2023-02-21 00:55:08.894536

#2
"""import datetime
x=datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
"""#2023 Tuesday

"""#3
import datetime
x=datetime.datetime(2023,2,21)
print(x)
"""

"""#4
import datetime
x=datetime.datetime.now()
print(x.strftime("%Y"))
print(x.strftime("%B"))
print(x.strftime("%X"))
"""

#math library:
"""
#1
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)"""

"""#2
x = abs(-7.25)
print(x)"""

"""#3
x=5
y=pow(5,2)
print(y)"""

"""#4
import math
x = math.sqrt(64)
print(x)"""

"""#5
import math
x = math.ceil(1.1)
y = math.floor(1.9)
print(x) # returns 2
print(y) # returns 1"""

"""#6
import math
x = math.pi
print(x)"""