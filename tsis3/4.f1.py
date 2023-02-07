def Primefilter(l, array):
    for i in range(len(l)):
        if l[i] == 1:
            continue
        t = True
        for j in range(2, l[i]):
            if l[i] % j == 0:
                t = False
                break
        if t == True:
            array.append(l[i])
    

l = [int(x) for x in input().split()]
array=[]
print(l)
Primefilter(l, array)
print(array)