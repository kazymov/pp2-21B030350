import re

txt=input()
x=re.findall("ab*",txt)
print(x)
#*-zero or more-ab,abbbbb....b