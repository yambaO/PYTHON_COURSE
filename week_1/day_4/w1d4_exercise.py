# ITP Week 1 Day 4 Exercise

# EASY

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 1. loop through the lowercase and print each element
for single_lowercase in lowercase:
    print(single_lowercase)

# 2. loop through the lowercase and print the capitalization of each element
for single_lowercase in lowercase:
    print(single_lowercase.upper())

# MEDIUM

# 1. create a new variable called uppercase with an empty list
# uppercase = []

# 2. loop through the lowercase list
    # 2a. append the capitalization of each element to the uppercase list

# for single_lowercase in lowercase:
# print(uppercase.append(single_lowercase))

# HARD

# A safe password has a minimum of (1) uppercase, (1) lowercase, (1) number, (1) special character.

password = "MySuperSafePassword!@34"

special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']


# 1. create the following variables and assign them Booleans as False
has_uppercase = False
has_lowercase = False
has_number = False
has_special_char = False

# 2. loop through the string password (same as a list)
for character in password:

# 3. For each iteration of the loop, create a if statement
# check to see if it exists in any of the list by using IN
# if it does exist, update the appropriate variable and CONTINUE
# not break.

 if character.isupper():
        has_uppercase = True
 elif character.islower():
  has_lowercase = True
 elif character.isdigit():
  has_number = True
 elif character in special_char:
  has_special_char = True
   
# NOTE: to see if it has a number, use range from 0 - 10!

# 4. do a final check to see if all of your variables are TRUE
# by using the AND operator for all 4 conditions. (This is done for you, uncomment below)

final_result = has_uppercase == True and has_lowercase == True and has_number == True and has_special_char == True
print(final_result)

# NOTE: we can shorthand this by just checking if the variable exists (returns True)
final_result_shorthand = has_uppercase and has_lowercase and has_number and has_special_char
print(final_result_shorthand)
# this will fail the same if any one of them is False

# If the final_result is true, print "SAFE STRONG PASSWORD"
# else, print "Update password: too weak"
# NOTE: this must be done outside of the loop
if final_result:
  print("SAFE STRONG PASSWORD")

else: print("Update password: too weak")  

# BONUS: update the password variable to take in an user input!

# NIGHTMARE: in the final check, use another if statement to list why it isn't a strong password!


