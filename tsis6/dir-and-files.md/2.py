import os

WORKING_DIR = os.getcwd()  #os.getcwd() method tells us the location of current working directory 

file_name = input()

path = os.path.join(WORKING_DIR, file_name)

if os.path.exists(path):
    print(f'Path "{path}" exists')
else:
    print(f'Path "{path} doesn\'t" exists')

if os.path.isfile(path) and os.access(path, os.R_OK): #os.path.isfile() method in Python is used to check whether the specified path is an existing regular file or not.
    print(f'Path "{path}" is readable')
else:
    print(f'Path "{path}" is not readable')

if os.path.isfile(path) and os.access(path, os.W_OK):
    print(f'Path "{path}" is writable')
else:
    print(f'Path "{path}" is now writable')

if os.access(path, os.X_OK):
    print(f'Path "{path}" is executable')
else:
    print(f'Path "{path}" is not executable')
    
    
    
    
# os.F_OK: проверяет наличие пути.
# os.R_OK: проверяет читаемость пути.
# os.W_OK: проверяет возможность записи пути.
# os.X_OK: проверяет, может ли быть выполнен путь.