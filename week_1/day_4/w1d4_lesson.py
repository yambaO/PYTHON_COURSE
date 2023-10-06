#CHANGE LIST ITEMS
# fruits = ["strawberry", "blackcurrant", "watermelon", "orange", "kiwi", "melon", "mango"]
# fruits[0] = "grapefruit"

#ADD LIST ITEMS
# end of the list
sports = ["football","soccer","baseball"]
sports.append("lacrosse")

#beginning of the list
sports.insert(3, " basketball")

#REMOVE ITEM
#remove item from beginning
sports.remove("lacrosse")
# print(sports)

#remove item from end
sports.pop()
# print(sports)

#del removes a specific index
del sports[1]
# print(sports)

#CLEAR THE LIST
# The clear () method empties the list

long_important_list = ['imagine', 'this', 'list', 'is', 'filled', 'with', 'important', 'stuff']
long_important_list.clear()