import re

txt=input()
x=re.findall("[A-Z][a-z]*",txt)

res=""
for i in x:
    res+=i+" "
    
print(res)