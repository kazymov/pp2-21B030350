def mygenerator(n):
    i=1
    while i*i<=num:
        yield i*i
        i+=1
    
num=int(input())
for x in mygenerator(num):
    print(x)