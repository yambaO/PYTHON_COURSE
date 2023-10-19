# ITP Week 3 Day 2 Practice

# 1. import the appropriate module

import json as js

json_1 = """
{
    "albumId": 1,
    "id": 1,
    "title": "accusamus beatae ad facilis cum similique qui sunt",
    "url": "https://via.placeholder.com/600/92c952",
    "thumbnailUrl": "https://via.placeholder.com/150/92c952"
}
"""


# 2. perform a deserialization of the above object
data = js.loads(json_1)

print(data)
# 3. assign a new variable called url_1 to the value of the deserialized object's url
url_1 = js.loads(json_1)["url"]
print(url_1)

json_2="""
[
{
"albumId": 1,
"id": 1,
"title": "accusamus beatae ad facilis cum similique qui sunt",
"url": "https://via.placeholder.com/600/92c952",
"thumbnailUrl": "https://via.placeholder.com/150/92c952"
},
{
"albumId": 1,
"id": 2,
"title": "reprehenderit est deserunt velit ipsam",
"url": "https://via.placeholder.com/600/771796",
"thumbnailUrl": "https://via.placeholder.com/150/771796"
}
]
"""
js.loads(json_2)

url_2 = js.loads(json_2)[0]["url"]
url_3 = js.loads(json_2)[2]["url"]

# 4. deserialize and assign a variable url_2 with the second item's url


