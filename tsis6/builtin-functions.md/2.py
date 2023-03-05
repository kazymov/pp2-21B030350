s = input()

uppers, lowers = 0, 0

for c in s:
    if ord(c) in range(65, 91):  #A-Z #ord->Convert an integer representing the Unicode of the specified character
        uppers += 1
    elif ord(c) in range(97, 123): #a-z
        lowers += 1

print(f'There are {uppers} upper case letters and {lowers} lower case letters')
