def mygenerator(n):
    i=n-1
    while i>=0:
        yield i
        i-=1
        
num=int(input())
for x in mygenerator(num):
    print(x)