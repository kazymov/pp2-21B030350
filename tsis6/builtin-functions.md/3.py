def Ispolindrom(s):
    for i in range(int(len(s)/2)):
        if s[i]!=s[-1-i]:
            return False
        
    return True

s=input()
if Ispolindrom(s):
    print(f' {s} is polindrom')
else:
    print(f'{s} is not polindrom')