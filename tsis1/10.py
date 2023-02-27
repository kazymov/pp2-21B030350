price=49
quantity=3
itemno=567
count=49
age=36
name="John"
txt1="The price is {:.2f} dollars"#amount of digits after comma
txt2="I want {} pieces of item number {} for {:.2f} dollars."
myorder1="I want {0} pieces of item number {1} for {2:.2f} dollars."
txt3="His name is {1}. {1} is {0} years old."
txt="Almaty {city}"
myorder="I have a {carname}, it is a {model}."
print(txt1.format(price))# push number in to the {}
print(txt2.format(quantity,itemno,count))
print(myorder1.format(quantity,itemno,count))
print(txt3.format(age, name))
print(myorder.format(carname="Ford", model="Mustang"))
print(txt.format(city="city"))
