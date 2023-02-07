def anspolindrom(str):
    l = 0
    r = len(str) - 1
    while l <= r:
        if not str[l] == str[r]:
            return False
        l += 1
        r -= 1
    return True

string = str(input())
print(anspolindrom(string))