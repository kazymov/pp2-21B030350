import os

path = input()

if os.path.exists(path):
    filename = os.path.basename(path) # basename->method in Python is used to get the base name in specified path. 
    print(f'The filename is "{filename}"')
    print(f'The directory portion is "{path.strip(filename)}"')  #strip=delete
else:
    print(f'Path "{path}" does not exists')