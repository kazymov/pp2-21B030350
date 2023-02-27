import re

txt=input()
x=re.findall("abbb?",txt)
print(x)
#?-from zero to one->ab,abb,abbb;