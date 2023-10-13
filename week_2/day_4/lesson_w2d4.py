# #DICTIONARY
# #Dictionaries are used to store data values in key:value pairs

# my_car = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year"  : 2021,
#     "interst" : 22
# }

# #Dictionary items are presented in key:value pairs and can be referred to by using the key name

# print(my_car["year"])

# #Dictionary Length
# print(len(my_car))

# # Dictionary Items - Data Types
# # String, int, boolean, and list data types:
your_car = {
  "brand": "Toyota",
  "model": "Prius",
  "electric": True,
  "year": 2012,
  "colors": ["red", "white", "blue"]
} 

# Accessing Items
your_car_brand = your_car["brand"]
your_car_brand = your_car.get("brand")

#Get Keys
key_list = your_car.keys()
