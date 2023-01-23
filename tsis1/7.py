#int:
x1=1
y1=3569854869856584
z1=-325684569

#float:
x2=1.10250
y2=1.0
z2=-35.59
x3=35e3
y3=12E4
z3=-87.7e100

#complex:
x4=3+5j
y4=5j
z4=-5j

#convert from one type to another:
a=float(x1)#convert fromt int to float
b=int(x2)#convert from float to int 
c=complex(x1)#convert from int to complex

#import random number:
import random

print(random.randrange(1, 10))
print(type(x1),type(x2),type(x3),type(x4))
print(type(y1),type(y2),type(y3),type(y4))
print(type(z1),type(z2),type(z3),type(z4))
print(a,":",type(a))
print(b,":",type(b))
print(c,":",type(c))
