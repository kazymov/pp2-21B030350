#permutations 
from itertools import permutations
def asnper(s):
    p = [''.join(p) for p in permutations(s)]
    return p
s = str(input())
print(asnper(s))