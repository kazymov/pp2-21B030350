l = list(
    ('18',
     '2004',
     'Ali',
     'Kazymov',
     'KBTU',
     'Spring Semester',
     'Faculty of information technologies'
     )
)

f = open('output.txt', 'w')

for s in l:
    f.write(s+'\n')