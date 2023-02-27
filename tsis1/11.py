print(10>9)#true
print(10==9)#FALSE
print(10<9)#false

a=200
b=33
if b>a:
    print("b is greater than a")
else:
    print("b is not greater then a")
    
print(bool("Hello"))
print(bool(15))
print(bool(["apple","cherry","banana"]))
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))#false because is empty
print(bool(()))
print(bool([]))
print(bool({}))


class myclass():
    def _len_(self):
        return 0
myobj=myclass()
print(bool(myobj))


#Functions can Return a Boolean
def myFunction() :
    return True
print(myFunction())

#boolean answer of function
def myFunction():
    return True
if myFunction():
    print("YES!")
else:
    print("NO!")
    
#Check if an object is an integer or not:
x=200
print(isinstance(x, int))
    