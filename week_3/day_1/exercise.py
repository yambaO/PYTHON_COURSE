# ITP Week 3 Day 1 Exercise

# ENUMERATE!

# 1. Read all instructions first!
# 
# Prompt: given a list of names, create a list of dictionaries with the index as the user_id and name

users_list = ["Alex", "Bob", "Charlie", "Dexter", "Edgar", "Frank", "Gary"]

# example output    
# [{"user_id": 0, "name": "Alex"}, etc, etc]
user_dictionararies = [{'user_id': 0, 'name': 'Alex'}, {'user_id': 1, 'name': 'Bob'}, {'user_id': 2, 'name': 'Charlie'}, {'user_id': 3, 'name': 'Dexter'}, {'user_id': 4, 'name': 'Edgar'}, {'user_id': 5, 'name': 'Frank'}, {'user_id': 6, 'name': 'Gary'}]


# 1a. Create a function that takes a single string value and returns the desired dictionary
def desired_dictionary(name):
    return {"name":name}


# 1b. Create a new empty list called users_dict_list
users_dict_list = []

# 1c. Loop through users_list that calls the function for each item and appends the return value to users_dict_list
for name in users_list:
    users_list = desired_dictionary(name)
    users_dict_list.append(users_list)
    # print(users_dict_list)
# 2. Prompt: Given a series of dictionaries and desired output (mock_data.py), can you provide the correct commands?
from mock_data import mock_data
# 2a. retrieve the gender of Morty Smith
print(mock_data["results"][1]["gender"])
# 2b. retrieve the length of the Rick Sanchez episodes
print(len(mock_data["results"][0]["episode"]))
# 2c. retrieve the url of Summer Smith location
print(mock_data["results"][2]["location"]["url"])