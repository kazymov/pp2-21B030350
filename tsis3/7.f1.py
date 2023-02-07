def determine3(l):
    for i in range(len(l)):
        if l[i] == 3 and l[i+1] == 3:
            return True
        else:
            return False


l= [int(x) for x in input().split()]
print(determine3(l))