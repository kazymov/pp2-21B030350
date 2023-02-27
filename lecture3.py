#functions
'''def myfunction (frame,lname):
     print(frame +" "+ lname)
    
myfunction("email", "tobias")
'''

'''def myfunction(*args):
    print("The youngest child is " + args[0])
myfunction("Emil", "Tobias", "Linus")
'''

'''def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
'''

'''def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
'''

'''def myfunction():
  pass
  '''
  
'''def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
'''

#lambda-sint:lambda arguments: expression
'''x = lambda a: a + 10
print(x(5))
'''

'''x = lambda a, b : a * b
print(x(5, 6))
'''

'''def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
'''


#classes and objects
'''class myclass:
  x=5
  str="february"
p1=myclass()
print(p1.str)
print(p1.x)
print(myclass)
'''

# _init_() function- to assign values
'''class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
'''

'''class Person:
  def _init_(self, name, age):
    self.name=name
    self=age=age
    
    
p1=Person("John", 36)

print(p1)
'''
'''
class Person:
  def __init__(self,name):
    self.firstname=name
  
  def str(self):
    print("Hello")
      
"""txt1=Person()
txt1.str()"""
txt2=Person("Ali")
print(txt2.firstname)
'''




