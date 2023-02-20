def mygenerators(n):
    i=0
    while i<n:
        if i%2==0:
            yield i
        i+=1
        
num=int(input())
for x in mygenerators(num):
    if x==num or x==num-1:
        print(x)
    else:
        print(x,end=",")