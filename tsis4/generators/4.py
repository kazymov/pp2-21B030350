def squares(a,b):
    for i in range(a,b+1):
        yield(i*i)
        if i>=b:
            break
a=int(input())
b=int(input())
for x in squares(a,b):
    print(x)