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
# your_car = {
#   "brand": "Toyota",
#   "model": "Prius",
#   "electric": True,
#   "year": 2012,
#   "colors": ["red", "white", "blue"]
# } 

# # Accessing Items
# your_car_brand = your_car["brand"]
# your_car_brand = your_car.get("brand")

# #Get Keys
# key_list = your_car.keys()

# # Get Values

# value_list = your_car.values()
# print(value_list) # dict_values(['Toyota', 'Pruis', True, 2012, ['red', 'white', 'blue']])
# print(type(value_list)) # <class 'dict_values'>*

# # Get Items

# item_list = your_car.items()
# print(item_list) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
# print(type(item_list)) # <class 'dict_items'>*

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

# x = car.keys()
# y = car.values()
# z = car.items()

# # before the change
# print(x)
# print(y)
# car["condition"] = "fair" # new key created
# car["year"] = 2018

# # after the change
# print(x)
# print(y)
# print(z)

# Check if Key Exists

# if "model" in car:
#     print("Yes, 'model' is one of the keys in the car dictionary") 


# Update Dictionary
car.update({"year" : 2020})
print(car)