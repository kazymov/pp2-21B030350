import time

num=int(input())
ms=int(input())

time.sleep(ms/1000) #Python time sleep() function suspends execution for the given number of seconds.
 
print(f'square root of {num} after {ms} milliseconds is  {num**0.5}')