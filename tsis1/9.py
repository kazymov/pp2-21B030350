a1="Hello"
a2="""Lorem ipsut dolar sit amet, consectetur adipisciing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
a3="Hello, World!"
print(a1)
print(a2)
print(a3[1])
print("Hello")
print('Hello')

#looping through a string 
for x in "banana":
    print(x, end="")# end=""-print on one line
    
print()

#string lenght
a="Hello, world!"
print(len(a))

#check string(in/not in) 
txt="The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present")
if "expensive" not in txt:
    print("NO, 'expensive' is NOT present.")