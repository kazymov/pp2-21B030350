import re

txt=input()

x = re.finditer('_?(?P<word>[a-z]+)_?', txt)


for w in x:
    print(w.group('word'))