# ITP Week 3 Day 2 Exercise

# import in the two modules for making API calls and parsing the data
import json as js
import requests as rq

# set a url variable to "https://rickandmortyapi.com/api/character"
url = "https://rickandmortyapi.com/api/character"

# set a variable response to the "get" request of the url
response = rq.get(url)
# print to verify we have a status code of 200
print(response)
# assign a variable json_data to the responses' json
json_data = response.json()
# print to verify a crazy body of strings!
posts =js.dumps(json_data, indent=2)
print(posts)
# lets make it into a python dictionary by using the appropriate json method
converted_json_dictionary = js.loads(posts)
# print the newly created python object
print(converted_json_dictionary)