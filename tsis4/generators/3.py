def mygenerator(n):
    i=0
    while i<n:
        if i%3==0 and i%4==0:
            yield i
        i+=1
num=int(input())
for x in mygenerator(num):
    print(x)