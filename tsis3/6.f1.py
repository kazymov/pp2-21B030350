def reversing(x):
    x.reverse()
        
s = str(input())
x = s.split()
reversing(x)
r = ' '.join(str(x) for x in x)
print(r)
