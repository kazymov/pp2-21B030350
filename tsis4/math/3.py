import math
n = int(input())
a = int(input())
s = 1
if n == 3:
    s = pow(a, 2)*math.sqrt(2)/4
elif n == 4:
    s = pow(a, 2)
else:
    s = n * pow(a, 2)/(4 * math.tan( math.pi/n ))
    
print(f"The area of the polygon is: {s}")