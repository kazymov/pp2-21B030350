def determine007(a):
  for i in range(len(a)):
    if a[i] == 0 and a[i+1] == 0 and a[i+2] == 7:
      return True
  return False

a= [int(x) for x in input().split()]
print(determine007(a))
