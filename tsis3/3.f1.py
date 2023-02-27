def Ans(numheads,numlegs):
    if numlegs%2!=0:
        return "error"
        
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:#i-chiken, j-rabbit
            return i,j
        
    return "error"# if i and j not found

numheads = int(input())
numlegs = int(input())
print(Ans(numheads, numlegs))


