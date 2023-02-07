def ansuniq(l):
    nl = []
    for i in l:
        if i not in nl:
            nl.append(i)
    return nl
l = [int(nl) for nl in input().split()]
print(ansuniq(l))