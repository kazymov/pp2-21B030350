#Dictionary- is a collection which is ordered*, changeable and do not allow duplicates.

'''#1 example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
'''

'''#2 example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
'''

'''
#3,4 examples
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(len(thisdict))
#{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}, 3
'''


'''
#4,5 example
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print(type(thisdict))
'''


'''#6 example
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
'''


cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
cars.pop(1)
print(cars)