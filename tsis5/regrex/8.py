import re

txt=input()

x=re.findall("[A-z][^A-Z]*",txt)
print(x)