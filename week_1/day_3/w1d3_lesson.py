#BOOLEANS

# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# we can use the bool() to evaluate any value

# print(bool("hello"))
# print(bool("15.5"))
# print(bool(""))
# print(bool(0.0))
# print(bool(0.1))

# COMPARISON OPERATORS

# a = 4  
# b = 5
# c = 5

# print( a == b)
# print( b == c)
# print(b != c)
# print( a > b)
# print( b > c)
# print( b >= c)

# LOGICAL OPERATORS

a = 4  
b = 5
c = 5
# if both side true , return true
print( a > 2 and b == c)
# if one side true, return true
print( a > 2 or b != c)


#IDENTITY OPERATORS

# is           Returns True if both variables are the same OBJECT                     x is y
# is not       Returns True if both variables are not the same OBJECT                x is not y

# obj1 = {'a': 'b'}

# obj2 = {'a': 'b'}

# obj1 == obj2 

# obj1 is obj2 

# IF / ELIF / ELSE STATEMENT

employee_id = 5048
if employee_id >= 9000:
 print("VIPs")
elif employee_id >= 8000:

    print("8th floor Executive")
elif employee_id >= 7000:
 print("7th floor Managers")
elif employee_id >= 6000:
 print("6th floor Sales")
elif employee_id >= 5000:
 # allowFifthFloorAccess()
 print("5th floor Operations")
elif employee_id >= 4000:

    print("4th floor Communications")
elif employee_id >= 3000:
 print("3rd floor Logistics")
elif employee_id >= 2000:
 print("2nd Floor Admin")
else:
 print("Lobby Security")